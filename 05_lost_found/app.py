"""Rank possible lost and found matches using transparent rules."""
import sys
import re
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import Store, form, heading, note, table, run

store = Store(Path(__file__).with_name('data.json'), {'reports': []})


def matches(report, reports):
    results = []
    words = set(re.findall(r'\w+', report['description'].lower()))
    for other in reports:
        if other['kind'] == report['kind'] or other['status'] == 'Returned':
            continue
        if other['category'].lower() != report['category'].lower():
            continue
        shared = words & set(re.findall(r'\w+', other['description'].lower()))
        score, reasons = 3, ['Same category']
        if shared:
            score += len(shared)
            reasons.append('Shared words: ' + ', '.join(sorted(shared)))
        if other['location'].lower() == report['location'].lower():
            score += 2
            reasons.append('Same location')
        gap = abs((date.fromisoformat(report['date']) -
                   date.fromisoformat(other['date'])).days)
        if gap <= 3:
            score += 1
            reasons.append('Dates within 3 days')
        results.append([other['id'], score, '; '.join(reasons), other['description']])
    return sorted(results, key=lambda row: (-row[1], row[0]))


def view():
    today = date.today().isoformat()
    out = note('Use sample descriptions without contact details. Matching suggests candidates; it does not prove ownership.')
    out += form('add', [('kind', 'Report type', 'select', ['Lost', 'Found']),
                        ('category', 'Category', 'text', 'Bottle'),
                        ('description', 'Description', 'text', 'Blue steel bottle'),
                        ('location', 'Location', 'text', 'Library'),
                        ('date', 'Date', 'date', today)], 'Add report')
    out += form('search', [('query', 'Category or description keyword', 'text', 'bottle')], 'Search reports')
    out += form('match', [('id', 'Lost or found report ID', 'number', '1')], 'Suggest matches')
    out += form('status', [('id', 'Report ID', 'number', '1'),
                           ('status', 'New status', 'select', ['Reported', 'Matched', 'Returned'])],
                'Update status')
    out += heading('All reports') + table(
        ['ID', 'Kind', 'Category', 'Description', 'Location', 'Date', 'Status'],
        [r.values() for r in store.data['reports']]
    )
    return out


def handle(data):
    records = store.data['reports']
    if data['action'] == 'add':
        date.fromisoformat(data['date'])
        if data['kind'] not in ['Lost', 'Found']:
            raise ValueError('Choose Lost or Found.')
        for key in ['category', 'description', 'location']:
            if not data[key].strip():
                raise ValueError('Text fields cannot be blank.')
        record = {'id': len(records) + 1, 'kind': data['kind'], 'category': data['category'].strip(),
                  'description': data['description'].strip(), 'location': data['location'].strip(),
                  'date': data['date'], 'status': 'Reported'}
        records.append(record)
    elif data['action'] == 'search':
        query = data['query'].strip().lower()
        found = [r.values() for r in records if query in (r['category'] + ' ' + r['description']).lower()]
        return heading('Filtered reports') + table(
            ['ID', 'Kind', 'Category', 'Description', 'Location', 'Date', 'Status'], found
        )
    elif data['action'] in ['match', 'status']:
        record = next((r for r in records if r['id'] == int(data['id'])), None)
        if record is None:
            raise ValueError('Report ID does not exist.')
        if data['action'] == 'match':
            if record['status'] == 'Returned':
                raise ValueError('This report is already closed.')
            return heading('Possible matches') + table(
                ['ID', 'Score', 'Reasons', 'Description'], matches(record, records)
            )
        if data['status'] not in ['Reported', 'Matched', 'Returned']:
            raise ValueError('Invalid status.')
        record['status'] = data['status']
    else:
        raise ValueError('Unknown action.')
    store.save()


if __name__ == '__main__':
    run('Campus Lost and Found Matcher', view, handle)
