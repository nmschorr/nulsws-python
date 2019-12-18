

from UserSettings import nulsws_USER_PARAMS
from UserSettings import nulsws_SET

all_set  = dir(nulsws_SET)
all_params = dir(nulsws_USER_PARAMS)
__ALL__  = all_set + all_params

print(__ALL__)


