from bottle import app

from .author import author_controller
from .authors import authors_controller
from .browse import browse_controller
from .code import code_controller
from .developers import developers_controller
from .docs import docs_controller
from .five_hundred import five_hundred_controller
from .four_oh_four import four_oh_four_controller
from .index import index_controller
from .installation import installation_controller
from .issues import issues_controller
from .label import label_controller
from .labels import labels_controller
from .new import new_controller
from .news import news_controller
from .package import package_controller
from .packages import packages_controller
from .popular import popular_controller
from .refresh_package import refresh_package_controller
from .rss import rss_controller
from .say_thanks import say_thanks_controller
from .search import search_controller
from .settings import settings_controller
from .stats import stats_controller
from .styles import styles_controller
from .submit import submit_controller
from .syncing import syncing_controller
from .trending import trending_controller
from .updated import updated_controller
from .usage import usage_controller