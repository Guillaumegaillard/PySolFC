##---------------------------------------------------------------------------##
##
## PySol -- a Python Solitaire game
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING.
## If not, write to the Free Software Foundation, Inc.,
## 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##
##---------------------------------------------------------------------------##

presets = {
    'None': {
        'preset': 'None',
        'name': n_('My Game'),
        },

    'Klondike': {
        'preset': 'Klondike',
        'name': n_('My Klondike'),
        'layout': 'Klondike',
        'talon': 'Deal to waste',
        'redeals': 'Unlimited redeals',
        'rows_num': 7,
        'rows_base_card': 'King',
        'reserves_num': 0,
        'deal_type': 'Triangle',
        'deal_face_down': 6,
        'deal_face_up': 1,
        },

    'FreeCell': {
        'preset': 'FreeCell',
        'name': n_('My FreeCell'),
        'skill_level': 'Mostly skill',
        'rows_max_move': 'Top card',
        'rows_super_move': 1,
        'deal_face_up': 6,
        },

    'Spider': {
        'preset': 'Spider',
        'name': n_('My Spider'),
        'skill_level': 'Mostly skill',
        'decks': 'Two',
        'layout': 'Klondike',
        'talon': 'Spider',
        'found_type': 'Spider same suit',
        'found_max_move': 'None',
        'rows_num': 10,
        'rows_type': 'Spider same suit',
        'reserves_num': 0,
        'deal_face_down': 5,
        'deal_face_up': 1,
        'deal_max_cards': 54,
        },

    'Gypsy': {
        'preset': 'Gypsy',
        'name': n_('My Gypsy'),
        'skill_level': 'Mostly skill',
        'decks': 'Two',
        'layout': 'Gypsy',
        'talon': 'Deal to tableau',
        'found_max_move': 'None',
        'reserves_num': 0,
        'deal_face_down': 2,
        'deal_face_up': 1,
        },

    'Ground for a Divorce': {
        'preset': 'Ground for a Divorce',
        'name': n_('My Ground for a Divorce'),
        'skill_level': 'Mostly skill',
        'decks': 'Two',
        'layout': 'Harp',
        'talon': 'Ground for a Divorce',
        'found_type': 'Spider same suit',
        'found_base_card': 'Any',
        'found_equal': 0,
        'rows_num': 10,
        'rows_type': 'Spider same suit',
        'rows_wrap': 1,
        'reserves_num': 0,
        'deal_face_up': 5,
        },

    'Double Klondike': {
        'preset': 'Double Klondike',
        'name': n_('My Double Klondike'),
        'decks': 'Two',
        'layout': 'Harp',
        'talon': 'Deal to waste',
        'redeals': 'Unlimited redeals',
        'rows_num': 9,
        'rows_base_card': 'King',
        'reserves_num': 0,
        'deal_type': 'Triangle',
        'deal_face_down': 8,
        'deal_face_up': 1,
        },

    'Simple Simon': {
        'preset': 'Simple Simon',
        'name': n_('My Simple Simon'),
        'skill_level': 'Mostly skill',
        'found_type': 'Spider same suit',
        'found_max_move': 'None',
        'rows_num': 10,
        'rows_type': 'Spider same suit',
        'reserves_num': 0,
        'deal_type': 'Triangle',
        },

}

