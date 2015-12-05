# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
WORDLIST=[
    'aback',
    'abase',
    'abash',
    'abate',
    'abbas',
    'abbey',
    'abbot',
    'abide',
    'abode',
    'abort',
    'about',
    'above',
    'abuse',
    'abyss',
    'acorn',
    'acrid',
    'actor',
    'acute',
    'adage',
    'adapt',
    'added',
    'addle',
    'adept',
    'adieu',
    'admit',
    'admix',
    'adobe',
    'adopt',
    'adore',
    'adorn',
    'adult',
    'aegis',
    'affix',
    'afire',
    'afoot',
    'afoul',
    'again',
    'agate',
    'agave',
    'agent',
    'agile',
    'aging',
    'agone',
    'agony',
    'agree',
    'ahead',
    'aisle',
    'alarm',
    'album',
    'alder',
    'aleph',
    'alert',
    'algae',
    'algal',
    'alias',
    'alibi',
    'alien',
    'align',
    'alike',
    'alive',
    'allay',
    'alley',
    'allot',
    'allow',
    'alloy',
    'allyl',
    'aloft',
    'aloha',
    'alone',
    'along',
    'aloof',
    'aloud',
    'alpha',
    'altar',
    'alter',
    'alway',
    'amass',
    'amaze',
    'amber',
    'amble',
    'amend',
    'amide',
    'amigo',
    'amino',
    'amiss',
    'amity',
    'among',
    'amort',
    'ample',
    'amply',
    'amuse',
    'anent',
    'angel',
    'anger',
    'angle',
    'angry',
    'angst',
    'anion',
    'anise',
    'ankle',
    'annal',
    'annex',
    'annoy',
    'annul',
    'annum',
    'anode',
    'antic',
    'anvil',
    'aorta',
    'apace',
    'apart',
    'aphid',
    'apple',
    'apply',
    'apron',
    'arena',
    'argon',
    'argot',
    'argue',
    'arhat',
    'arise',
    'aroma',
    'arose',
    'array',
    'arrow',
    'arson',
    'ashen',
    'aside',
    'askew',
    'aspen',
    'assai',
    'assay',
    'asset',
    'aster',
    'atlas',
    'atone',
    'attic',
    'audio',
    'audit',
    'auger',
    'augur',
    'aural',
    'auric',
    'avail',
    'avert',
    'avoid',
    'await',
    'awake',
    'award',
    'aware',
    'awash',
    'awful',
    'awoke',
    'axial',
    'axiom',
    'azure',
    'bacon',
    'badge',
    'bagel',
    'baggy',
    'baldy',
    'balky',
    'balmy',
    'balsa',
    'banal',
    'bandy',
    'banjo',
    'barge',
    'baron',
    'barre',
    'basal',
    'basic',
    'basil',
    'basin',
    'basis',
    'bassi',
    'basso',
    'baste',
    'batch',
    'bater',
    'bathe',
    'batik',
    'baton',
    'bawdy',
    'bayed',
    'bayou',
    'beach',
    'beady',
    'beard',
    'beast',
    'beaux',
    'bebop',
    'bedim',
    'beech',
    'beefy',
    'befit',
    'began',
    'beget',
    'begin',
    'begun',
    'beige',
    'being',
    'belch',
    'belie',
    'belle',
    'belly',
    'below',
    'beman',
    'bench',
    'beret',
    'berne',
    'berry',
    'berth',
    'beryl',
    'beset',
    'betel',
    'bevel',
    'bezel',
    'bicep',
    'biddy',
    'bigot',
    'bilge',
    'billy',
    'binge',
    'biota',
    'birch',
    'birth',
    'bison',
    'bitch',
    'black',
    'blade',
    'blame',
    'blanc',
    'bland',
    'blank',
    'blare',
    'blast',
    'blaze',
    'bleak',
    'bleat',
    'bleed',
    'blend',
    'bless',
    'blest',
    'blimp',
    'blind',
    'blink',
    'bliss',
    'blitz',
    'bloat',
    'block',
    'bloke',
    'blond',
    'blood',
    'bloom',
    'bloop',
    'blown',
    'bluet',
    'bluff',
    'blunt',
    'blurb',
    'blurt',
    'blush',
    'board',
    'boast',
    'bobby',
    'bogey',
    'boggy',
    'bogus',
    'bongo',
    'bonus',
    'bonze',
    'booby',
    'booky',
    'boost',
    'booth',
    'booty',
    'booze',
    'borax',
    'boric',
    'borne',
    'boron',
    'bosom',
    'boson',
    'botch',
    'bough',
    'boule',
    'bound',
    'bourn',
    'bowel',
    'bowie',
    'boyar',
    'brace',
    'bract',
    'braid',
    'brain',
    'brake',
    'brand',
    'brant',
    'brash',
    'brass',
    'brave',
    'bravo',
    'brawl',
    'bread',
    'break',
    'bream',
    'breed',
    'breve',
    'briar',
    'bribe',
    'brick',
    'bride',
    'brief',
    'brine',
    'bring',
    'brink',
    'briny',
    'brisk',
    'broad',
    'broil',
    'broke',
    'brood',
    'brook',
    'broom',
    'broth',
    'brown',
    'bruit',
    'brunt',
    'brush',
    'brute',
    'buddy',
    'budge',
    'buggy',
    'bugle',
    'build',
    'built',
    'bulge',
    'bulky',
    'bully',
    'bunch',
    'bundy',
    'bunny',
    'buret',
    'burly',
    'burnt',
    'burro',
    'burst',
    'buses',
    'bushy',
    'butch',
    'buteo',
    'butte',
    'butyl',
    'buxom',
    'buyer',
    'buzzy',
    'bylaw',
    'byway',
    'cabal',
    'cabin',
    'cable',
    'cacao',
    'cache',
    'cacti',
    'caddy',
    'cadet',
    'cadre',
    'cagey',
    'cairn',
    'calla',
    'calve',
    'camel',
    'cameo',
    'canal',
    'candy',
    'canna',
    'canny',
    'canoe',
    'canon',
    'canst',
    'canto',
    'caper',
    'caret',
    'cargo',
    'carne',
    'carob',
    'carol',
    'carry',
    'carte',
    'carve',
    'caste',
    'catch',
    'cater',
    'caulk',
    'cause',
    'cavil',
    'cease',
    'cedar',
    'chafe',
    'chaff',
    'chain',
    'chair',
    'chalk',
    'champ',
    'chant',
    'chaos',
    'chard',
    'charm',
    'chart',
    'chase',
    'chasm',
    'cheap',
    'cheat',
    'check',
    'cheek',
    'cheer',
    'chert',
    'chess',
    'chest',
    'chevy',
    'chick',
    'chide',
    'chief',
    'child',
    'chili',
    'chill',
    'chime',
    'china',
    'chine',
    'chink',
    'chirp',
    'chive',
    'chock',
    'choir',
    'choke',
    'chomp',
    'chord',
    'chore',
    'chose',
    'chuck',
    'chuff',
    'chump',
    'chunk',
    'churn',
    'chute',
    'cider',
    'cigar',
    'cilia',
    'cinch',
    'circa',
    'civet',
    'civic',
    'civil',
    'claim',
    'clamp',
    'clang',
    'clank',
    'clash',
    'clasp',
    'class',
    'clean',
    'clear',
    'cleat',
    'cleft',
    'clerk',
    'click',
    'cliff',
    'climb',
    'clime',
    'cling',
    'clink',
    'cloak',
    'clock',
    'clomp',
    'clone',
    'close',
    'cloth',
    'cloud',
    'clout',
    'clove',
    'clown',
    'cluck',
    'clump',
    'clung',
    'coach',
    'coast',
    'cobra',
    'cocky',
    'cocoa',
    'codon',
    'colon',
    'colza',
    'comet',
    'comic',
    'comma',
    'conch',
    'coney',
    'conic',
    'cooky',
    'copra',
    'coral',
    'corny',
    'corps',
    'cosec',
    'coset',
    'cotta',
    'cotty',
    'couch',
    'cough',
    'could',
    'count',
    'coupe',
    'court',
    'coven',
    'cover',
    'covet',
    'cowry',
    'coypu',
    'cozen',
    'crack',
    'craft',
    'cramp',
    'crane',
    'crank',
    'crash',
    'crass',
    'crate',
    'crave',
    'crawl',
    'craze',
    'crazy',
    'creak',
    'cream',
    'credo',
    'creed',
    'creek',
    'creep',
    'crepe',
    'crept',
    'cress',
    'crest',
    'cried',
    'crime',
    'crimp',
    'crisp',
    'criss',
    'croak',
    'crock',
    'croft',
    'crone',
    'crony',
    'crook',
    'croon',
    'cross',
    'crowd',
    'crown',
    'crude',
    'cruel',
    'crumb',
    'crump',
    'crush',
    'crust',
    'crypt',
    'csnet',
    'cubic',
    'culpa',
    'cumin',
    'curia',
    'curie',
    'curio',
    'curry',
    'curse',
    'curve',
    'cycad',
    'cycle',
    'cynic',
    'daddy',
    'daffy',
    'dairy',
    'daisy',
    'dally',
    'dance',
    'dandy',
    'dater',
    'datum',
    'daunt',
    'davit',
    'dealt',
    'death',
    'debar',
    'debit',
    'debug',
    'debut',
    'decal',
    'decay',
    'decor',
    'decoy',
    'decry',
    'defer',
    'degas',
    'degum',
    'deify',
    'deign',
    'deity',
    'delay',
    'delta',
    'delve',
    'demit',
    'demon',
    'demur',
    'dense',
    'depot',
    'depth',
    'derby',
    'deter',
    'deuce',
    'devil',
    'dewar',
    'diary',
    'dicta',
    'diety',
    'digit',
    'dingo',
    'dingy',
    'diode',
    'dirge',
    'dirty',
    'disco',
    'ditch',
    'ditto',
    'ditty',
    'divan',
    'dizzy',
    'dodge',
    'dogma',
    'dolce',
    'dolly',
    'donor',
    'doubt',
    'douce',
    'dough',
    'douse',
    'dowel',
    'dowry',
    'dozen',
    'draft',
    'drain',
    'drake',
    'drama',
    'drank',
    'drape',
    'drawl',
    'drawn',
    'dread',
    'dream',
    'dress',
    'dried',
    'drier',
    'drift',
    'drill',
    'drink',
    'drive',
    'droll',
    'drone',
    'drool',
    'droop',
    'dross',
    'drove',
    'drown',
    'druid',
    'drunk',
    'dryad',
    'ducat',
    'dully',
    'dulse',
    'dummy',
    'dumpy',
    'dunce',
    'dusky',
    'dusty',
    'dwarf',
    'dwell',
    'dwelt',
    'dying',
    'eager',
    'eagle',
    'earth',
    'easel',
    'eaten',
    'eater',
    'ebony',
    'eclat',
    'edict',
    'edify',
    'eerie',
    'egret',
    'eider',
    'eight',
    'eject',
    'elate',
    'elbow',
    'elder',
    'elect',
    'elegy',
    'elfin',
    'elide',
    'elite',
    'elope',
    'elude',
    'elute',
    'elves',
    'embed',
    'ember',
    'emcee',
    'empty',
    'endow',
    'enemy',
    'enter',
    'entry',
    'envoy',
    'epoch',
    'epoxy',
    'equal',
    'equip',
    'erase',
    'erect',
    'erode',
    'error',
    'erupt',
    'essay',
    'ester',
    'estop',
    'ether',
    'ethic',
    'ethos',
    'ethyl',
    'etude',
    'eucre',
    'evade',
    'event',
    'every',
    'evict',
    'evoke',
    'exact',
    'exalt',
    'excel',
    'exert',
    'exile',
    'exist',
    'expel',
    'extol',
    'extra',
    'exude',
    'exult',
    'fable',
    'facet',
    'facto',
    'faery',
    'faint',
    'fairy',
    'faith',
    'false',
    'fancy',
    'farad',
    'farce',
    'fatal',
    'fatty',
    'fault',
    'fauna',
    'feast',
    'feign',
    'feint',
    'felon',
    'femur',
    'fence',
    'ferry',
    'fetal',
    'fetch',
    'fetid',
    'fetus',
    'fever',
    'fiche',
    'field',
    'fiend',
    'fiery',
    'fifth',
    'fifty',
    'fight',
    'filch',
    'filet',
    'filly',
    'filmy',
    'filth',
    'final',
    'finch',
    'finny',
    'first',
    'fishy',
    'fjord',
    'flack',
    'flail',
    'flair',
    'flake',
    'flaky',
    'flame',
    'flank',
    'flare',
    'flash',
    'flask',
    'fleck',
    'fleet',
    'flesh',
    'flick',
    'flier',
    'fling',
    'flint',
    'flirt',
    'float',
    'flock',
    'flood',
    'floor',
    'flora',
    'flour',
    'flout',
    'flown',
    'fluff',
    'fluid',
    'fluke',
    'flung',
    'flunk',
    'flush',
    'flute',
    'flyer',
    'foamy',
    'focal',
    'focus',
    'foggy',
    'foist',
    'folio',
    'folly',
    'foray',
    'force',
    'forge',
    'forgo',
    'forte',
    'forth',
    'forty',
    'forum',
    'found',
    'fount',
    'fovea',
    'foyer',
    'frail',
    'frame',
    'franc',
    'frank',
    'fraud',
    'freak',
    'freed',
    'freer',
    'freon',
    'fresh',
    'friar',
    'fried',
    'frill',
    'frock',
    'front',
    'frost',
    'froth',
    'frown',
    'froze',
    'fruit',
    'fudge',
    'fugal',
    'fugue',
    'fully',
    'fungi',
    'funny',
    'furry',
    'furze',
    'fussy',
    'fusty',
    'fuzzy',
    'gable',
    'gaffe',
    'gamin',
    'gamma',
    'gamut',
    'gases',
    'gassy',
    'gator',
    'gaudy',
    'gauge',
    'gaunt',
    'gauss',
    'gauze',
    'gavel',
    'gawky',
    'gecko',
    'geese',
    'genie',
    'genii',
    'genre',
    'genus',
    'ghost',
    'ghoul',
    'giant',
    'gibby',
    'giddy',
    'gimpy',
    'girth',
    'given',
    'glade',
    'gland',
    'glans',
    'glare',
    'glass',
    'glaze',
    'gleam',
    'glean',
    'glide',
    'glint',
    'gloat',
    'globe',
    'gloom',
    'glory',
    'gloss',
    'glove',
    'glued',
    'gluey',
    'glyph',
    'gnarl',
    'gnash',
    'gnome',
    'golly',
    'goody',
    'goofy',
    'goose',
    'gorge',
    'gorse',
    'gouge',
    'gourd',
    'grace',
    'grade',
    'graft',
    'grail',
    'grain',
    'grand',
    'grant',
    'grape',
    'graph',
    'grasp',
    'grass',
    'grata',
    'grate',
    'grave',
    'gravy',
    'graze',
    'great',
    'grebe',
    'greed',
    'green',
    'greet',
    'grief',
    'grill',
    'grime',
    'grind',
    'gripe',
    'grist',
    'groan',
    'groat',
    'groin',
    'groom',
    'grope',
    'gross',
    'group',
    'grout',
    'grove',
    'growl',
    'grown',
    'gruff',
    'grunt',
    'guano',
    'guard',
    'guess',
    'guest',
    'guide',
    'guild',
    'guile',
    'guilt',
    'guise',
    'gules',
    'gully',
    'gumbo',
    'gummy',
    'gunky',
    'gunny',
    'gusto',
    'gusty',
    'gutsy',
    'gypsy',
    'habit',
    'haiku',
    'hairy',
    'halma',
    'halve',
    'handy',
    'happy',
    'hardy',
    'harem',
    'harry',
    'harsh',
    'haste',
    'hasty',
    'hatch',
    'hater',
    'haunt',
    'haven',
    'havoc',
    'hazel',
    'heady',
    'heard',
    'heart',
    'heath',
    'heave',
    'heavy',
    'hedge',
    'hefty',
    'heigh',
    'helix',
    'hello',
    'hence',
    'henry',
    'heron',
    'hertz',
    'hilly',
    'hilum',
    'hinge',
    'hippo',
    'hippy',
    'hitch',
    'hoagy',
    'hoard',
    'hobby',
    'hocus',
    'hodge',
    'hogan',
    'holly',
    'hondo',
    'honey',
    'hooch',
    'horde',
    'horny',
    'horse',
    'hotel',
    'hough',
    'hound',
    'house',
    'hovel',
    'hover',
    'howdy',
    'hubby',
    'human',
    'humid',
    'humus',
    'hunch',
    'hurry',
    'hurty',
    'husky',
    'hutch',
    'hydra',
    'hydro',
    'hyena',
    'hying',
    'hymen',
    'ideal',
    'idiom',
    'idiot',
    'idyll',
    'igloo',
    'ileum',
    'iliac',
    'image',
    'imbue',
    'impel',
    'inane',
    'inapt',
    'incur',
    'index',
    'inept',
    'inert',
    'infer',
    'infix',
    'infra',
    'ingot',
    'inlay',
    'inlet',
    'inner',
    'input',
    'inset',
    'inter',
    'inure',
    'ionic',
    'irate',
    'irony',
    'issue',
    'ivory',
    'jazzy',
    'jelly',
    'jenny',
    'jerky',
    'jerry',
    'jewel',
    'jiffy',
    'jimmy',
    'joint',
    'jolly',
    'joule',
    'joust',
    'jowly',
    'judge',
    'juice',
    'juicy',
    'julep',
    'jumbo',
    'jumpy',
    'junco',
    'junky',
    'junta',
    'juror',
    'kapok',
    'kappa',
    'karma',
    'kazoo',
    'kelly',
    'kerry',
    'ketch',
    'keyed',
    'khaki',
    'kinky',
    'kiosk',
    'kitty',
    'knack',
    'knead',
    'kneel',
    'knell',
    'knelt',
    'knick',
    'knife',
    'knock',
    'knoll',
    'known',
    'knurl',
    'koala',
    'kodak',
    'kombu',
    'kraft',
    'kraut',
    'kudzu',
    'kulak',
    'label',
    'labia',
    'laden',
    'ladle',
    'lager',
    'laity',
    'lance',
    'lanky',
    'lapel',
    'lapse',
    'larch',
    'large',
    'larva',
    'lasso',
    'latch',
    'later',
    'latex',
    'lathe',
    'latus',
    'laugh',
    'laura',
    'layup',
    'leach',
    'leafy',
    'leaky',
    'leapt',
    'learn',
    'lease',
    'leash',
    'least',
    'leave',
    'ledge',
    'leech',
    'leery',
    'lefty',
    'legal',
    'leggy',
    'lemma',
    'lemon',
    'leper',
    'levee',
    'level',
    'lever',
    'lewis',
    'libel',
    'light',
    'liken',
    'lilac',
    'limbo',
    'limit',
    'linen',
    'lingo',
    'lipid',
    'lisle',
    'lithe',
    'liven',
    'livid',
    'livre',
    'loamy',
    'loath',
    'lobar',
    'lobby',
    'local',
    'locus',
    'lodge',
    'loess',
    'lofty',
    'logic',
    'lolly',
    'loose',
    'lossy',
    'lotus',
    'louse',
    'lousy',
    'lower',
    'loyal',
    'lucid',
    'lucky',
    'lucre',
    'luger',
    'lumen',
    'lumpy',
    'lunar',
    'lunch',
    'lunge',
    'lurch',
    'lurid',
    'lusty',
    'lying',
    'lymph',
    'lynch',
    'lyric',
    'macho',
    'macro',
    'madam',
    'magic',
    'magma',
    'magna',
    'major',
    'mambo',
    'mamma',
    'mange',
    'mania',
    'manic',
    'manna',
    'manor',
    'manse',
    'maple',
    'march',
    'maria',
    'marry',
    'marsh',
    'maser',
    'mason',
    'match',
    'mater',
    'matte',
    'mauve',
    'maxim',
    'maybe',
    'mayor',
    'mayst',
    'mealy',
    'meant',
    'meaty',
    'mecum',
    'medal',
    'media',
    'medic',
    'melee',
    'melon',
    'mercy',
    'merge',
    'merit',
    'merry',
    'meson',
    'messy',
    'metal',
    'meter',
    'metro',
    'mezzo',
    'micro',
    'midge',
    'midst',
    'might',
    'milch',
    'milky',
    'mimic',
    'mince',
    'minim',
    'minor',
    'minot',
    'minus',
    'mirth',
    'miser',
    'misty',
    'mitre',
    'mixup',
    'modal',
    'model',
    'modem',
    'modus',
    'moire',
    'moist',
    'molal',
    'molar',
    'mommy',
    'monad',
    'monel',
    'money',
    'monic',
    'monte',
    'month',
    'moody',
    'moose',
    'moral',
    'morel',
    'moron',
    'mossy',
    'motel',
    'motet',
    'motif',
    'motor',
    'motto',
    'mould',
    'mound',
    'mount',
    'mourn',
    'mouse',
    'mousy',
    'mouth',
    'movie',
    'mucus',
    'muddy',
    'muggy',
    'mugho',
    'mulch',
    'mulct',
    'multi',
    'mummy',
    'munch',
    'mural',
    'murky',
    'murre',
    'mushy',
    'music',
    'musty',
    'mylar',
    'mynah',
    'myrrh',
    'nabla',
    'nadir',
    'naiad',
    'naive',
    'naked',
    'nasal',
    'nasty',
    'natal',
    'natty',
    'naval',
    'navel',
    'neath',
    'needy',
    'nerve',
    'never',
    'newel',
    'niche',
    'niece',
    'night',
    'ninth',
    'nitty',
    'noble',
    'nodal',
    'noise',
    'noisy',
    'nomad',
    'nonce',
    'noose',
    'north',
    'notch',
    'novel',
    'nudge',
    'nurse',
    'nylon',
    'nymph',
    'oaken',
    'oases',
    'oasis',
    'obese',
    'objet',
    'occur',
    'ocean',
    'octal',
    'octet',
    'odium',
    'offal',
    'offer',
    'often',
    'ohmic',
    'olden',
    'olive',
    'omega',
    'onion',
    'onset',
    'opera',
    'opine',
    'opium',
    'optic',
    'orate',
    'orbit',
    'order',
    'organ',
    'osier',
    'other',
    'otter',
    'ought',
    'ounce',
    'ouvre',
    'ouzel',
    'ovary',
    'ovate',
    'overt',
    'owing',
    'oxeye',
    'oxide',
    'ozone',
    'paddy',
    'padre',
    'paean',
    'pagan',
    'paint',
    'palsy',
    'pampa',
    'panda',
    'panel',
    'panic',
    'pansy',
    'panty',
    'papal',
    'papaw',
    'paper',
    'pappy',
    'parch',
    'parry',
    'parse',
    'party',
    'pasha',
    'passe',
    'paste',
    'pasty',
    'patch',
    'pater',
    'patio',
    'patty',
    'pause',
    'peace',
    'peach',
    'peaky',
    'pearl',
    'pecan',
    'pedal',
    'peepy',
    'penal',
    'pence',
    'penis',
    'penna',
    'penny',
    'peony',
    'peppy',
    'perch',
    'peril',
    'perky',
    'peste',
    'petal',
    'petit',
    'petri',
    'petty',
    'pewee',
    'phage',
    'phase',
    'phlox',
    'phone',
    'phony',
    'photo',
    'phyla',
    'piano',
    'picky',
    'piece',
    'piety',
    'piggy',
    'pilot',
    'pinch',
    'pinto',
    'pious',
    'pique',
    'pitch',
    'pithy',
    'pivot',
    'pixel',
    'pizza',
    'place',
    'plaid',
    'plain',
    'plane',
    'plank',
    'plant',
    'plasm',
    'plate',
    'playa',
    'plaza',
    'plead',
    'pleat',
    'pluck',
    'plumb',
    'plume',
    'plump',
    'plunk',
    'plush',
    'poach',
    'pocus',
    'podge',
    'podia',
    'poesy',
    'point',
    'poise',
    'polar',
    'polio',
    'polis',
    'polka',
    'pooch',
    'poppy',
    'porch',
    'posey',
    'posit',
    'posse',
    'pouch',
    'pound',
    'power',
    'prank',
    'preen',
    'press',
    'prexy',
    'price',
    'prick',
    'pride',
    'prima',
    'prime',
    'primp',
    'print',
    'prior',
    'prism',
    'privy',
    'prize',
    'probe',
    'prone',
    'prong',
    'proof',
    'prose',
    'proud',
    'prove',
    'prowl',
    'proxy',
    'prune',
    'psalm',
    'psych',
    'puffy',
    'pulse',
    'punch',
    'punky',
    'pupal',
    'pupil',
    'puppy',
    'purge',
    'purse',
    'pussy',
    'putty',
    'pygmy',
    'quack',
    'quaff',
    'quail',
    'quake',
    'qualm',
    'quark',
    'quart',
    'quash',
    'quasi',
    'queen',
    'queer',
    'quell',
    'query',
    'quest',
    'queue',
    'quick',
    'quiet',
    'quill',
    'quilt',
    'quint',
    'quirk',
    'quirt',
    'quite',
    'quota',
    'quote',
    'rabat',
    'rabbi',
    'rabid',
    'radar',
    'radii',
    'radio',
    'radix',
    'radon',
    'rainy',
    'raise',
    'rajah',
    'rally',
    'ranch',
    'randy',
    'range',
    'rangy',
    'rapid',
    'rater',
    'ratio',
    'ratty',
    'ravel',
    'raven',
    'razor',
    'reach',
    'ready',
    'realm',
    'reave',
    'rebel',
    'rebut',
    'recur',
    'reedy',
    'reeve',
    'refer',
    'regal',
    'reign',
    'relic',
    'reman',
    'remit',
    'renal',
    'repel',
    'resin',
    'retch',
    'revel',
    'rever',
    'revet',
    'rheum',
    'rhino',
    'rhyme',
    'ridge',
    'rifle',
    'right',
    'rigid',
    'rilly',
    'rinse',
    'ripen',
    'risen',
    'risky',
    'rival',
    'riven',
    'river',
    'rivet',
    'roach',
    'roast',
    'robin',
    'robot',
    'rocky',
    'rodeo',
    'rogue',
    'rondo',
    'rooky',
    'roomy',
    'roost',
    'rotor',
    'rouge',
    'rough',
    'round',
    'rouse',
    'route',
    'rowdy',
    'royal',
    'ruddy',
    'rumen',
    'rummy',
    'runic',
    'runty',
    'rupee',
    'rural',
    'rusty',
    'rutty',
    'sable',
    'sabra',
    'saint',
    'salad',
    'sally',
    'salon',
    'salty',
    'salve',
    'salvo',
    'samba',
    'sandy',
    'sappy',
    'satan',
    'satin',
    'satyr',
    'sauce',
    'saucy',
    'saute',
    'savoy',
    'savvy',
    'scald',
    'scale',
    'scalp',
    'scamp',
    'scant',
    'scare',
    'scarf',
    'scary',
    'scaup',
    'scene',
    'scent',
    'scion',
    'scoff',
    'scold',
    'scoop',
    'scoot',
    'scope',
    'scops',
    'score',
    'scorn',
    'scour',
    'scout',
    'scowl',
    'scram',
    'scrap',
    'screw',
    'scrim',
    'scrub',
    'scuba',
    'scuff',
    'scull',
    'seamy',
    'sedan',
    'seder',
    'sedge',
    'seedy',
    'seize',
    'senor',
    'sense',
    'sepal',
    'sepia',
    'septa',
    'serge',
    'serif',
    'serum',
    'serve',
    'servo',
    'setup',
    'seven',
    'sever',
    'shack',
    'shade',
    'shady',
    'shaft',
    'shake',
    'shako',
    'shaky',
    'shale',
    'shall',
    'shame',
    'shank',
    'shape',
    'shard',
    'share',
    'shark',
    'sharp',
    'shave',
    'shawl',
    'sheaf',
    'shear',
    'sheen',
    'sheep',
    'sheer',
    'sheet',
    'sheik',
    'shelf',
    'shell',
    'shied',
    'shift',
    'shill',
    'shine',
    'shiny',
    'shire',
    'shirk',
    'shirt',
    'shish',
    'shoal',
    'shock',
    'shoji',
    'shone',
    'shook',
    'shoot',
    'shore',
    'short',
    'shout',
    'shove',
    'shown',
    'showy',
    'shred',
    'shrew',
    'shrub',
    'shrug',
    'shuck',
    'shunt',
    'sibyl',
    'sidle',
    'siege',
    'sieve',
    'sight',
    'sigma',
    'silky',
    'silly',
    'silty',
    'since',
    'sinew',
    'singe',
    'sinus',
    'siren',
    'sisal',
    'situs',
    'sixth',
    'sixty',
    'skate',
    'skeet',
    'skied',
    'skiff',
    'skill',
    'skimp',
    'skirt',
    'skulk',
    'skull',
    'skunk',
    'slack',
    'slain',
    'slake',
    'slang',
    'slant',
    'slash',
    'slate',
    'slave',
    'sleek',
    'sleep',
    'sleet',
    'slept',
    'slice',
    'slick',
    'slide',
    'slime',
    'slimy',
    'sling',
    'sloop',
    'slope',
    'slosh',
    'sloth',
    'slump',
    'slung',
    'slurp',
    'smack',
    'small',
    'smart',
    'smash',
    'smear',
    'smell',
    'smelt',
    'smile',
    'smirk',
    'smith',
    'smoke',
    'smoky',
    'snack',
    'snafu',
    'snail',
    'snake',
    'snare',
    'snark',
    'snarl',
    'sneak',
    'sneer',
    'snell',
    'snick',
    'sniff',
    'snipe',
    'snook',
    'snoop',
    'snore',
    'snort',
    'snout',
    'snowy',
    'snuff',
    'soapy',
    'sober',
    'soggy',
    'solar',
    'solid',
    'solve',
    'somal',
    'sonar',
    'sonic',
    'sonny',
    'sooth',
    'sorry',
    'sough',
    'sound',
    'south',
    'space',
    'spade',
    'spare',
    'spark',
    'spasm',
    'spate',
    'spawn',
    'speak',
    'spear',
    'speck',
    'speed',
    'spell',
    'spend',
    'spent',
    'sperm',
    'spice',
    'spicy',
    'spike',
    'spiky',
    'spill',
    'spilt',
    'spine',
    'spiny',
    'spire',
    'spite',
    'spitz',
    'splat',
    'splay',
    'split',
    'spoil',
    'spoke',
    'spoof',
    'spook',
    'spool',
    'spoon',
    'spore',
    'sport',
    'spout',
    'spray',
    'spree',
    'sprig',
    'sprue',
    'spume',
    'spunk',
    'spurn',
    'spurt',
    'squad',
    'squat',
    'squaw',
    'squid',
    'stack',
    'staff',
    'stage',
    'stagy',
    'staid',
    'stain',
    'stair',
    'stake',
    'stale',
    'stalk',
    'stall',
    'stamp',
    'stand',
    'stank',
    'staph',
    'stare',
    'stark',
    'start',
    'stash',
    'state',
    'stave',
    'stead',
    'steak',
    'steal',
    'steam',
    'steed',
    'steel',
    'steep',
    'steer',
    'stein',
    'stern',
    'stick',
    'stiff',
    'stile',
    'still',
    'stilt',
    'sting',
    'stink',
    'stint',
    'stock',
    'stoic',
    'stoke',
    'stole',
    'stomp',
    'stone',
    'stony',
    'stood',
    'stool',
    'stoop',
    'store',
    'stork',
    'storm',
    'story',
    'stout',
    'stove',
    'strap',
    'straw',
    'stray',
    'strip',
    'strop',
    'strum',
    'strut',
    'stuck',
    'study',
    'stuff',
    'stump',
    'stung',
    'stunk',
    'stunt',
    'style',
    'styli',
    'suave',
    'sugar',
    'suite',
    'sulfa',
    'sulky',
    'sully',
    'sumac',
    'sunny',
    'super',
    'supra',
    'surge',
    'sushi',
    'swage',
    'swain',
    'swami',
    'swamp',
    'swank',
    'swarm',
    'swart',
    'swath',
    'swear',
    'sweat',
    'sweep',
    'sweet',
    'swell',
    'swelt',
    'swept',
    'swift',
    'swine',
    'swing',
    'swipe',
    'swirl',
    'swish',
    'swiss',
    'swoop',
    'sword',
    'swore',
    'sworn',
    'swung',
    'synod',
    'syrup',
    'table',
    'taboo',
    'tacit',
    'tacky',
    'taffy',
    'taint',
    'taken',
    'talky',
    'tally',
    'talon',
    'talus',
    'tango',
    'tangy',
    'tansy',
    'taper',
    'tapir',
    'tapis',
    'tappa',
    'tardy',
    'tarry',
    'taste',
    'tasty',
    'tater',
    'tatty',
    'taunt',
    'tawny',
    'teach',
    'tease',
    'tecum',
    'teeth',
    'tempo',
    'tempt',
    'tenet',
    'tenon',
    'tenor',
    'tense',
    'tenth',
    'tepee',
    'tepid',
    'terry',
    'terse',
    'testy',
    'thank',
    'theft',
    'their',
    'theme',
    'there',
    'these',
    'theta',
    'thick',
    'thief',
    'thigh',
    'thine',
    'thing',
    'think',
    'third',
    'thong',
    'thorn',
    'those',
    'three',
    'threw',
    'throb',
    'throw',
    'thrum',
    'thumb',
    'thump',
    'thyme',
    'tibet',
    'tibia',
    'tidal',
    'tiger',
    'tight',
    'tilde',
    'tilth',
    'timid',
    'tinge',
    'tippy',
    'tipsy',
    'tithe',
    'title',
    'toady',
    'toast',
    'today',
    'token',
    'tommy',
    'tonal',
    'tonic',
    'tooth',
    'topaz',
    'topic',
    'torah',
    'torch',
    'torso',
    'torus',
    'total',
    'totem',
    'touch',
    'tough',
    'towel',
    'tower',
    'toxic',
    'toxin',
    'trace',
    'track',
    'tract',
    'trade',
    'trail',
    'train',
    'trait',
    'tramp',
    'trash',
    'trawl',
    'tread',
    'treat',
    'trend',
    'tress',
    'triac',
    'triad',
    'trial',
    'tribe',
    'trick',
    'tried',
    'trill',
    'tripe',
    'trite',
    'troll',
    'troop',
    'trout',
    'truce',
    'truck',
    'truly',
    'trump',
    'trunk',
    'truss',
    'trust',
    'truth',
    'tulip',
    'tulle',
    'tunic',
    'tuple',
    'turvy',
    'tutor',
    'twain',
    'tweak',
    'tweed',
    'twice',
    'twill',
    'twine',
    'twirl',
    'twist',
    'tying',
    'typic',
    'ulcer',
    'ultra',
    'umber',
    'umbra',
    'unary',
    'uncle',
    'under',
    'unify',
    'union',
    'unite',
    'unity',
    'until',
    'upend',
    'upper',
    'upset',
    'urban',
    'urine',
    'usage',
    'usher',
    'usual',
    'usurp',
    'usury',
    'utile',
    'utter',
    'vacua',
    'vacuo',
    'vague',
    'valet',
    'valid',
    'value',
    'valve',
    'vapid',
    'vault',
    'vaunt',
    'veery',
    'velar',
    'veldt',
    'venal',
    'venom',
    'verge',
    'versa',
    'verse',
    'verve',
    'vetch',
    'vicar',
    'video',
    'vigil',
    'villa',
    'vinyl',
    'viola',
    'virus',
    'visit',
    'visor',
    'vista',
    'vitae',
    'vital',
    'vitro',
    'vivid',
    'vixen',
    'vocal',
    'vogue',
    'voice',
    'vomit',
    'vouch',
    'vowel',
    'vying',
    'wacke',
    'wacky',
    'wafer',
    'waist',
    'waive',
    'waken',
    'wally',
    'waltz',
    'warty',
    'washy',
    'waste',
    'watch',
    'water',
    'waxen',
    'weary',
    'weave',
    'weber',
    'wedge',
    'weedy',
    'weigh',
    'weird',
    'welsh',
    'whack',
    'whale',
    'wharf',
    'wheat',
    'wheel',
    'whelk',
    'whelm',
    'whelp',
    'where',
    'which',
    'whiff',
    'while',
    'whine',
    'whirl',
    'whish',
    'whisk',
    'white',
    'whole',
    'whoop',
    'whore',
    'whose',
    'widen',
    'widow',
    'width',
    'wield',
    'wince',
    'winch',
    'windy',
    'wishy',
    'wispy',
    'witch',
    'withe',
    'withy',
    'witty',
    'wolve',
    'woman',
    'women',
    'woody',
    'wordy',
    'world',
    'wormy',
    'worry',
    'worse',
    'worst',
    'worth',
    'would',
    'wound',
    'woven',
    'wrack',
    'wrath',
    'wreak',
    'wreck',
    'wrest',
    'wring',
    'wrist',
    'write',
    'wrong',
    'wrote',
    'xenon',
    'xerox',
    'xylem',
    'yacht',
    'yearn',
    'yeast',
    'yield',
    'yodel',
    'yokel',
    'young',
    'youth',
    'yucca',
    'zazen',
    'zebra',
    'zesty',
    'zilch',
    'zippy',
    'zloty'
]

def index():
    """
    Splash page
    """
    return dict()


def instructions():

    return dict()


def wordlist():
    """
    List of all words used in the game
    """
    rows = db(db.wordList.id > 0).select(db.wordList.word)
    word_list = [r.word for r in rows]
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    y = []
    z = []
    for word in word_list:
        if word[0] == 'a':
            a.append(word)
        if word[0] == 'b':
            b.append(word)
        if word[0] == 'c':
            c.append(word)
        if word[0] == 'd':
            d.append(word)
        if word[0] == 'e':
            e.append(word)
        if word[0] == 'f':
            f.append(word)
        if word[0] == 'g':
            g.append(word)
        if word[0] == 'h':
            h.append(word)
        if word[0] == 'i':
            i.append(word)
        if word[0] == 'j':
            j.append(word)
        if word[0] == 'k':
            k.append(word)
        if word[0] == 'l':
            l.append(word)
        if word[0] == 'm':
            m.append(word)
        if word[0] == 'n':
            n.append(word)
        if word[0] == 'o':
            o.append(word)
        if word[0] == 'p':
            p.append(word)
        if word[0] == 'q':
            q.append(word)
        if word[0] == 'r':
            r.append(word)
        if word[0] == 's':
            s.append(word)
        if word[0] == 't':
            t.append(word)
        if word[0] == 'u':
            u.append(word)
        if word[0] == 'v':
            v.append(word)
        if word[0] == 'w':
            w.append(word)
        if word[0] == 'x':
            x.append(word)
        if word[0] == 'y':
            y.append(word)
        if word[0] == 'z':
            z.append(word)
    return dict(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m,
                n=n, o=o, p=p, q=q, r=r, s=s, t=t, u=u, v=v, w=w, x=x, y=y, z=z)


def board():
    """
    List of playable games
    """
    return dict()


def game():
    """
    Individual game
    """
    game = db(db.games.id == request.args(0)).select().first()
    rows = db().select(db.wordList.ALL)
    d = [r.word for r in rows]
    return dict(targetWord=game.targetWord)


def load_wordlist():
    """
    Loads the list of words
    """
    rows = db().select(db.wordList.ALL)
    d = [r.word for r in rows]
    return response.json(dict(wordList=d))



def add_game():
    """
    Adds a game to the database
    Removes a game name from the database
    """
    db.games.update_or_insert(targetWord = request.vars.targetWord)
    db(db.game_names.word == request.vars.targetWord).delete()
    return 'ok'


def load_games():
    """
    Loads the list of created games
    """
    rows = db().select(db.games.ALL)
    d = {r.id: {'word': r.targetWord} for r in rows}
    return response.json(dict(games=d))


def load_game_names():
    """
    Loads the list of available game names
    """
    rows = db().select(db.game_names.ALL)
    d2 = [r.word for r in rows]
    return response.json(dict(game_names=d2))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


