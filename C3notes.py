from reaper_python import *

global notesname_array
###########################################################
#
# GLOBALS
#
###########################################################
notesname_instruments_array = {
    "PART DRUMS" : "DRUMS",
    "PART GUITAR" : "5LANES",
    "PART BASS" : "5LANES",
    "PART VOCALS" : "VOCALS",
    "PART KEYS" : "5LANES",
    "PART REAL_KEYS_X": "PROKEYS",
    "PART REAL_KEYS_H": "PROKEYS",
    "PART REAL_KEYS_M": "PROKEYS",
    "PART REAL_KEYS_E": "PROKEYS",
    "PART KEYS_ANIM_LH": "PROKEYS",
    "PART KEYS_ANIM_RH": "PROKEYS",
    "HARM1": "VOCALS",
    "HARM2": "VOCALS",
    "HARM3": "VOCALS",
    "PART DRUMS 2X": "DRUMS",
    "PART RHYTHM": "5LANES",
    "PART REAL_GUITAR": "PROGUITAR",
    "PART REAL_GUITAR_22": "PROGUITAR",
    "PART REAL_BASS": "PROGUITAR",
    "PART REAL_BASS_22": "PROGUITAR"
    }

notesname_array = {
    "5LANES" :
    {
    127 : ["TRILL MARKER", "markers"],
    126 : ["TREMOLO MARKER", "markers"],
    124 : ["BRE", "bre"],
    123 : ["BRE", "bre"],
    122 : ["BRE", "bre"],
    121 : ["BRE", "bre"],
    120 : ["BRE", "bre"],
    116 : ["Overdrive", "od"],
    103 : ["Solo Marker", "solo"],
    102 : ["Expert Force HOPO Off", "markers"],
    101 : ["Expert Force HOPO On", "markers"],
    100 : ["Expert Orange", "notes_x", "O"],
    99 : ["Expert Blue", "notes_x", "B"],
    98 : ["Expert Yellow", "notes_x", "Y"],
    97 : ["Expert Red", "notes_x", "R"],
    96 : ["Expert Green", "notes_x", "G"],			
    90 : ["Force HOPO Off", "markers"],
    89 : ["Force HOPO On", "markers"],
    88 : ["Hard Orange", "notes_h", "O"],
    87 : ["Hard Blue", "notes_h", "B"],
    86 : ["Hard Yellow", "notes_h", "Y"],
    85 : ["Hard Red", "notes_h", "R"],
    84 : ["Hard Green", "notes_h", "G"],
    78 : ["Medium Force HOPO Off", "markers"],
    77 : ["Medium Force HOPO On", "markers"],
    76 : ["Medium Orange", "notes_m", "O"],
    75 : ["Medium Blue", "notes_m", "B"],
    74 : ["Medium Yellow", "notes_m", "Y"],
    73 : ["Medium Red", "notes_m", "R"],
    72 : ["Medium Green", "notes_m", "G"],
    64 : ["Easy Orange", "notes_e", "O"],
    63 : ["Easy Blue", "notes_e", "B"],
    62 : ["Easy Yellow", "notes_e", "Y"],
    61 : ["Easy Red", "notes_e", "R"],
    60 : ["Easy Green", "notes_e", "G"],
    59 : ["Left Hand Highest", "animations"],
    58 : ["Left Hand Highest 2", "animations"],
    57 : ["Left Hand Highest 3", "animations"],
    56 : ["Left Hand Highest 4", "animations"],
    55 : ["Left Hand Highest 5", "animations"],
    54 : ["Left Hand Highest 6", "animations"],
    53 : ["Left Hand Highest 7", "animations"],
    52 : ["Left Hand Highest 8", "animations"],
    51 : ["Left Hand Highest 9", "animations"],
    50 : ["Left Hand Highest 10", "animations"],
    49 : ["Left Hand Highest 11", "animations"],
    48 : ["Left Hand Highest 12", "animations"],
    47 : ["Left Hand Highest 13", "animations"],
    46 : ["Left Hand Highest 14", "animations"],
    45 : ["Left Hand Highest 15", "animations"],
    44 : ["Left Hand Highest 16", "animations"],
    43 : ["Left Hand Highest 17", "animations"],
    42 : ["Left Hand Highest 18", "animations"],
    41 : ["Left Hand Highest 19", "animations"],
    40 : ["Left Hand Lowest", "animations"]
    },
    "DRUMS" :
    {
        127 : ["Cymbal Swell", "markers"],
	126 : ["Drum Roll", "markers"],
	124 : ["Drum Fill Green", "bre"],
	123 : ["Drum Fill Blue", "bre"],
	122 : ["Drum Fill Yellow", "bre"],
	121 : ["Drum Fill Red", "bre"],
	120 : ["Drum Fill Orange", "bre"],
	116 : ["Overdrive", "od"],
	112 : ["Toms Gems Green", "markers", "G"],
	111 : ["Tom Gems Blue", "markers", "B"],
	110 : ["Toms Gems Yellow", "markers", "Y"],
	103 : ["Solo Marker", "solo"],
	100 : ["Expert Green", "notes_x", "G"],
	99 : ["Expert Blue", "notes_x", "B"],
	98 : ["Expert Yellow", "notes_x", "Y"],
	97 : ["Expert Red", "notes_x", "R"],
	96 : ["Expert Kick", "notes_x", "O"],
	88 : ["Hard Green", "notes_h", "G"],
	87 : ["Hard Blue", "notes_h", "B"],
	86 : ["Hard Yellow", "notes_h", "Y"],
	85 : ["Hard Red", "notes_h", "R"],
	84 : ["Hard Kick", "notes_h", "O"],
	76 : ["Medium Green", "notes_m", "G"],
	75 : ["Medium Blue", "notes_m", "B"],
	74 : ["Medium Yellow", "notes_m", "Y"],
	73 : ["Medium Red", "notes_m", "R"],
	72 : ["Medium Kick", "notes_m", "O"],
	64 : ["Easy Green", "notes_e", "G"],
	63 : ["Easy Blue", "notes_e", "B"],
	62 : ["Easy Yellow", "notes_e", "Y"],
	61 : ["Easy Red", "notes_e", "R"],
	60 : ["Easy Kick", "notes_e", "O"],
	51 : ["Anim. Floort Tom RH", "animations"],
	50 : ["Anim. Floor Tom LH", "animations"],
	49 : ["Anim. TOM2 RH", "animations"],
	48 : ["Anim. TOM2 LH", "animations"],
	47 : ["Anim. TOM1 RH", "animations"],
	46 : ["Anim. TOM1 LH", "animations"],
	45 : ["Anim. SOFT CRASH 2 LH", "animations"],
	44 : ["Anim. CRASH 2 LH", "animations"],
	43 : ["Anim. RIDE LH", "animations"],
	42 : ["Anim. RIDE CYM RH", "animations"],
	41 : ["Anim. CRASH2 CHOKE", "animations"],
	40 : ["Anim. CRASH1 CHOKE", "animations"],
	39 : ["Anim. CRASH2 SOFT RH", "animations"],
	38 : ["Anim. CRASH2 HARD RH", "animations"],
	37 : ["Anim. CRASH1 SOFT RH", "animations"],
	36 : ["Anim. CRASH1 HARD RH", "animations"],
	35 : ["Anim. CRASH1 SOFT LH", "animations"],
	34 : ["Anim. CRASH1 HARD LH", "animations"],
	33 : ["Anim. ", "animations"],
	32 : ["Anim. PERCUSSION RH", "animations"],
	31 : ["Anim. HI-HAT RH", "animations"],
	30 : ["Anim. HI-HAT LH", "animations"],
	29 : ["Anim. SOFT SNARE RH", "animations"],
	28 : ["Anim. SOFT SNARE LH", "animations"],
	27 : ["Anim. SNARE RH", "animations"],
	26 : ["Anim. SNARE LH", "animations"],
	25 : ["Anim. HI-HAT OPEN", "animations"],
	24 : ["Anim. KICK RF", "animations"]
    },
    "VOCALS" :
    {
	116: ["Overdrive", "od"],
	105: ["Phrase Marker", "phrase"],
	97:	["Non-Displayed Percussion", "percussion"],
	96:	["Displayed Percussion", "percussion"],
	83:	["Highest Note B5", "notes"],
	82:	["A#4", "notes"],
	81:	["A4", "notes"],
	80:	["G#4", "notes"],
	79:	["G4", "notes"],
	78:	["F#4", "notes"],
	77:	["F4", "notes"],
	76:	["E4", "notes"],
	75:	["D#4", "notes"],
	74:	["D4", "notes"],
	73:	["C#4", "notes"],
	72:	["C4", "notes"],
	71:	["B3", "notes"],
	70:	["A#3", "notes"],
	69:	["A3", "notes"],
	68:	["G#3", "notes"],
	67:	["G3", "notes"],
	66:	["F#3", "notes"],
	65:	["F3", "notes"],
	64:	["E3", "notes"],
	63:	["D#3", "notes"],
	62:	["D3", "notes"],
	61:	["C#3", "notes"],
	60:	["C3", "notes"],
	59:	["B2", "notes"],
	58:	["A#2", "notes"],
	57:	["A2", "notes"],
	56:	["G#2", "notes"],
	55:	["G2", "notes"],
	54:	["F#2", "notes"],
	53:	["F2", "notes"],
	52:	["E2", "notes"],
	51:	["D#2", "notes"],
	50:	["D2", "notes"],
	49:	["C#2", "notes"],
	48:	["C2", "notes"],
	47:	["B1", "notes"],
	46:	["A#1", "notes"],
	45:	["A1", "notes"],
	44:	["G#1", "notes"],
	43:	["G1", "notes"],
	42:	["F#1", "notes"],
	41:	["F1", "notes"],
	40:	["E1", "notes"],
	39:	["D#1", "notes"],
	38:	["D1", "notes"],
	37:	["C#1", "notes"],
	36:	["Lowest Note C1", "notes"],
	1:	["Lyric Shift", "shift"],
	0:	["Range Shift", "shift"]
    },
    "PROKEYS" :
    {
        127 : ["TRILL MARKER", "markers"],
        126 : ["GLISSANDO MARKER", "markers"],
	124 : ["BRE", "bre"], 
	123 : ["BRE", "bre"],
	122 : ["BRE", "bre"],
	121 : ["BRE", "bre"], 
	120 : ["BRE", "bre"],
	116: ["Overdrive", "od"],
	115: ["Solo Marker", "solo"],	
	72:	["C4", "notes"],
	71:	["B3", "notes"],
	70:	["A#3", "notes"],
	69:	["A3", "notes"],
	68:	["G#3", "notes"],
	67:	["G3", "notes"],
	66:	["F#3", "notes"],
	65:	["F3", "notes"],
	64:	["E3", "notes"],
	63:	["D#3", "notes"],
	62:	["D3", "notes"],
	61:	["C#3", "notes"],
	60:	["C3", "notes"],
	59:	["B2", "notes"],
	58:	["A#2", "notes"],
	57:	["A2", "notes"],
	56:	["G#2", "notes"],
	55:	["G2", "notes"],
	54:	["F#2", "notes"],
	53:	["F2", "notes"],
	52:	["E2", "notes"],
	51:	["D#2", "notes"],
	50:	["D2", "notes"],
	49:	["C#2", "notes"],
	48:	["C2", "notes"],
	9:	["Range A2-C4", "shift"],
	7:	["Range G2-B3", "shift"],
	5:	["Range F2-A3", "shift"],
	4:	["Range E2-G3", "shift"],
	2:	["Range D2-F3", "shift"],
	0:	["Range C2-C3", "shift"]
    },
    "PROGUITAR" :
    {
        127 : ["TRILL MARKER", "markers"],
        126 : ["TREMOLO MARKER", "markers"],
        125 : ["BRE", "bre"],
        124 : ["BRE", "bre"],
        123 : ["BRE", "bre"],
        122 : ["BRE", "bre"],
        121 : ["BRE", "bre"],
        120 : ["BRE", "bre"],
        116 : ["Overdrive", "od"],
        115 : ["Solo Marker", "solo"],
        108 : ["LEFT HAND POSITION", "fhp"],
        107 : ["Force Chord Number", "markers"],
        105 : ["Expert Strum Direction", "markers"],
        104 : ["Expert Arpeggio Marker", "markers"],
        103 : ["Expert Slider Marker", "markers"],
        102 : ["Expert Force HOPO On", "markers"],
        101 : ["Expert E String (High)", "notes_x"],
        100 : ["Expert B String", "notes_x"],
        99 : ["Expert G String", "notes_x"],
        98 : ["Expert D String", "notes_x"],
        97 : ["Expert A String", "notes_x",],
        96 : ["Expert E String (Low)", "notes_x"],
        81 : ["Hard Strum Direction", "markers"],
        80 : ["Hard Arpeggio Marker", "markers"],
        79 : ["Hard Slider Marker", "markers"],
        78 : ["Hard Force HOPO On", "markers"],
        77 : ["Hard E String (High)", "notes_h"],
        76 : ["Hard B String", "notes_h"],
        75 : ["Hard G String", "notes_h"],
        74 : ["Hard D String", "notes_h"],
        73 : ["Hard A String", "notes_h"],
        72 : ["Hard E String (Low)", "notes_h"],
        56 : ["Medium Arpeggio Marker", "markers"],
        55 : ["Medium Slider Marker", "markers"],
        54 : ["Medium Force HOPO On", "markers"],
        53 : ["Medium E String (High)", "notes_m"],
        52 : ["Medium B String", "notes_m"],
        51 : ["Medium G String", "notes_m"],
        50 : ["Medium D String", "notes_m"],
        49 : ["Medium A String", "notes_m"],
        48 : ["Medium E String (Low)", "notes_m"],
        31 : ["Easy Slider Marker", "markers"],
        29 : ["Easy E String (High)", "notes_e"],
        28 : ["Easy B String", "notes_e"],
        27 : ["Easy G String", "notes_e"],
        26 : ["Easy D String", "notes_e"],
        25 : ["Easy A String", "notes_e"],
        24 : ["Easy E String (Low)", "notes_e"],
        17 : ["Hide Chord Names", "markers"],
        16 : ["Slash Chord", "markers"],
        15 : ["Eb root note", "root_notes"],
        14 : ["D root note", "root_notes"],
        13 : ["Db root note", "root_notes"],
        12 : ["C root note", "root_notes"],
        11 : ["B root note", "root_notes"],
        10 : ["Bb root note", "root_notes"],
        9 : ["A root note", "root_notes"],
        8 : ["Ab root note", "root_notes"],
        7 : ["G root note", "root_notes"],
        6 : ["Gb root note", "root_notes"],
        5 : ["F root note", "root_notes"],
        4 : ["E root note", "root_notes"]
    }
    }
