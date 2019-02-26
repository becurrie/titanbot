"""
constant.py

Store any bot specific values here that should not change at any point.
"""
from settings import LOG_DIR
import re
import datetime

# Game statistics tuple used as keys/attribute names.
STATS_GAME_STAT_KEYS = (
    "highest_stage_reached",
    "total_pet_level",
    "gold_earned",
    "taps",
    "titans_killed",
    "bosses_killed",
    "critical_hits",
    "chestersons_killed",
    "prestiges",
    "play_time",
    "relics_earned",
    "fairies_tapped",
    "daily_achievements",
)

# Bot statistics tuple  used as keys/attribute names.
STATS_BOT_STAT_KEYS = (
    "premium_ads",
    "clan_ship_battles",
    "actions",
    "updates",
)

# JSON dictionary template used by the stats module to feed into an empty json file
# if one doesn't already exist on initialization.
STATS_JSON_TEMPLATE = {
    "game_statistics": {},
    "bot_statistics": {},
    "artifact_statistics": {},
    "sessions": {}
}

# The lookup multiplier is used to convert in game values that are formatted with specific multipliers
# (K, M, T) into their respective float values, or the closest we can get to the actual value. These
# values can then be parsed and diffed.
STATS_LOOKUP_MULTIPLIER = {
    'K': 10**3,
    'M': 10**6,
}

# Regex used to extract the days, hours, minutes and seconds out of the strings used in game to
# determine time deltas.
STATS_DURATION_RE = re.compile(
    r'^((?P<days>[.\d]+?)d) ?((?P<hours>[.\d]+?):)?((?P<minutes>[.\d]+?):)?((?P<seconds>[.\d]+?)?$)'
)

# Format string used when converting time delta objects back into their respective format found in game.
STATS_TIMEDELTA_STR = "{D}d {H}:{M}:{S}"
# Stats date format for session keys.
STATS_DATE_FMT = "%Y-%m-%d"
# Logger name used when grabbing logger.
LOGGER_NAME = "tt2_py"
# Logging format string.
LOGGER_FORMAT = "[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"
# Logging file name format string here.
LOGGER_FILE_NAME_STRFMT = "%Y-%m-%d_%H-%M-%S"
INIT_DATE_FMT = datetime.datetime.strftime(datetime.datetime.now(), LOGGER_FILE_NAME_STRFMT)
LOGGER_FILE_NAME = "{log_dir}/{name}.log".format(log_dir=LOG_DIR, name=INIT_DATE_FMT)

# imagesearch.py will make use of these constants to determine which button to press.
LEFT_CLICK = "left"
RIGHT_CLICK = "right"
MIDDLE_CLICK = "middle"

# Threshold used to determine if the value of the next parsed stage is obviously malformed.
# This can be determined by looking at the new value, subtracting it from the old value and seeing
# if it crosses the threshold, in which case we can skip the current parse attempt.
STAGE_PARSE_THRESHOLD = 10000

# Determine how many loops are possible before giving up functionality
# (due to an error in game that causes the ui to lag and the bot to miss an image check).
# Now, ideally, no UI errors should come up if the bots functionality is working as intended.
# Although some issues still sneak as every use case can not be totally locked down. This is a final fallback.
# Also, this value represents the UPPER limit of a failed case. Since some loops may take numerous attempts
# before succeeding (artifact scrolling in particular). So this can be set to a decently large value.
FUNCTION_LOOP_TIMEOUT = 40
