import sys
from datetime import datetime
from pathlib import Path

import numpy as np

from .spiritus import _cola

a_list = [
    'Marco',
    'Polo',
    'Hello',
    'World',
    'Yup',
    'Nope',
    'Maybe',
    'Sure',
    'Ok',
    'Yes',
    'No',
    'Absolutely',
    'Definitely',
    'Certainly',
    'Affirmative',
    'Negative',
    'Indeed',
    'Perhaps',
    'Possibly',
    'Likely',
    'Unlikely',
    'Certainly Not',
    'Without a Doubt',
    'For Sure',
    'Indubitably',
    'Undoubtedly',
    'Sure Thing',
    'You Bet',
    'By All Means',
    'Of Course',
    'Naturally',
    'Evidently',
    'Clearly',
    'Obviously',
    'Manifestly',
    'Plainly',
    'Patently',
    'Unquestionably',
    'Irrefutably',
    'Incontrovertibly',
    'Categorically',
    'Decidedly',
    'Unequivocally',
    'Positively',
    'Absolutely Not',
    'Definitely Not',
    'Certainly Not',
    'Indisputably',
    'Unmistakably',
    'Undeniably',
    'Inarguably',
    'Incontestably',
    'Irrevocably',
    'Unalterably',
    'Unchangeably',
    'Immutably',
    'Perpetually',
    'Eternally',
    'Everlastingly',
    'Endlessly',
    'Ceaselessly',
    'Incessantly',
    'Continuously',
    'Relentlessly',
    'Persistently',
    'Tenaciously',
    'Doggedly',
    'Steadfastly',
]


def yup() -> list[str]:
    a_list.append('Yup!')
    print('yup!')
    np.random.rand(5)
    pathy = Path('sone') / 'path' / 'here'
    sys.stdout.write(f'Path: {pathy}\n')
    _cola()
    time = datetime.now().isoformat()
    print(f'Current time: {time}')
    return a_list


def _float_to_int(user_float: float) -> int:
    return int(user_float)
