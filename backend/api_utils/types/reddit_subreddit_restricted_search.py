from enum import Enum
from typing import List, Optional, Any, Union
from uuid import UUID


class AuthorFlairType(Enum):
    RICHTEXT = "richtext"
    TEXT = "text"


class LinkFlairText(Enum):
    DUPLICATE_REPOST = "Duplicate/Repost"
    ELMWOOD_VILLAGE = "Elmwood Village"
    QUESTION = "Question"
    THINGS_TO_DO = "Things To Do"


class FlairRichtext:
    e: AuthorFlairType
    t: LinkFlairText

    def __init__(self, e: AuthorFlairType, t: LinkFlairText) -> None:
        self.e = e
        self.t = t


class FlairTextColor(Enum):
    DARK = "dark"
    LIGHT = "light"


class Domain(Enum):
    SELF_BUFFALO = "self.Buffalo"


class Facets:
    pass

    def __init__(self, ) -> None:
        pass


class WhitelistStatus(Enum):
    ALL_ADS = "all_ads"


class Subreddit(Enum):
    BUFFALO = "Buffalo"


class SubredditID(Enum):
    T5_2_QI6_I = "t5_2qi6i"


class SubredditNamePrefixed(Enum):
    R_BUFFALO = "r/Buffalo"


class SubredditType(Enum):
    PUBLIC = "public"


class SuggestedSort(Enum):
    CONTROVERSIAL = "controversial"
    TOP = "top"


class Thumbnail(Enum):
    SELF = "self"


class PostData:
    approved_at_utc: None
    subreddit: Subreddit
    selftext: str
    author_fullname: str
    saved: bool
    mod_reason_title: None
    gilded: int
    clicked: bool
    title: str
    link_flair_richtext: List[FlairRichtext]
    subreddit_name_prefixed: SubredditNamePrefixed
    hidden: bool
    pwls: int
    link_flair_css_class: Optional[str]
    downs: int
    thumbnail_height: None
    top_awarded_type: None
    hide_score: bool
    name: str
    quarantine: bool
    link_flair_text_color: FlairTextColor
    upvote_ratio: float
    author_flair_background_color: Optional[str]
    subreddit_type: SubredditType
    ups: int
    total_awards_received: int
    media_embed: Facets
    thumbnail_width: None
    author_flair_template_id: Optional[UUID]
    is_original_content: bool
    user_reports: List[Any]
    secure_media: None
    is_reddit_media_domain: bool
    is_meta: bool
    category: None
    secure_media_embed: Facets
    link_flair_text: Optional[LinkFlairText]
    can_mod_post: bool
    score: int
    approved_by: None
    is_created_from_ads_ui: bool
    author_premium: bool
    thumbnail: Thumbnail
    edited: Union[bool, int]
    author_flair_css_class: None
    author_flair_richtext: List[FlairRichtext]
    gildings: Facets
    content_categories: None
    is_self: bool
    mod_note: None
    created: int
    link_flair_type: AuthorFlairType
    wls: int
    removed_by_category: None
    banned_by: None
    author_flair_type: AuthorFlairType
    domain: Domain
    allow_live_comments: bool
    selftext_html: str
    likes: None
    suggested_sort: Optional[SuggestedSort]
    banned_at_utc: None
    view_count: None
    archived: bool
    no_follow: bool
    is_crosspostable: bool
    pinned: bool
    over_18: bool
    all_awardings: List[Any]
    awarders: List[Any]
    media_only: bool
    can_gild: bool
    spoiler: bool
    locked: bool
    author_flair_text: Optional[str]
    treatment_tags: List[Any]
    visited: bool
    removed_by: None
    num_reports: None
    distinguished: None
    subreddit_id: SubredditID
    author_is_blocked: bool
    mod_reason_by: None
    removal_reason: None
    link_flair_background_color: str
    id: str
    is_robot_indexable: bool
    report_reasons: None
    author: str
    discussion_type: None
    num_comments: int
    send_replies: bool
    whitelist_status: WhitelistStatus
    contest_mode: bool
    mod_reports: List[Any]
    author_patreon_flair: bool
    author_flair_text_color: Optional[FlairTextColor]
    permalink: str
    parent_whitelist_status: WhitelistStatus
    stickied: bool
    url: str
    subreddit_subscribers: int
    created_utc: int
    num_crossposts: int
    media: None
    is_video: bool
    link_flair_template_id: Optional[UUID]

    def __init__(self, approved_at_utc: None, subreddit: Subreddit, selftext: str, author_fullname: str, saved: bool, mod_reason_title: None, gilded: int, clicked: bool, title: str, link_flair_richtext: List[FlairRichtext], subreddit_name_prefixed: SubredditNamePrefixed, hidden: bool, pwls: int, link_flair_css_class: Optional[str], downs: int, thumbnail_height: None, top_awarded_type: None, hide_score: bool, name: str, quarantine: bool, link_flair_text_color: FlairTextColor, upvote_ratio: float, author_flair_background_color: Optional[str], subreddit_type: SubredditType, ups: int, total_awards_received: int, media_embed: Facets, thumbnail_width: None, author_flair_template_id: Optional[UUID], is_original_content: bool, user_reports: List[Any], secure_media: None, is_reddit_media_domain: bool, is_meta: bool, category: None, secure_media_embed: Facets, link_flair_text: Optional[LinkFlairText], can_mod_post: bool, score: int, approved_by: None, is_created_from_ads_ui: bool, author_premium: bool, thumbnail: Thumbnail, edited: Union[bool, int], author_flair_css_class: None, author_flair_richtext: List[FlairRichtext], gildings: Facets, content_categories: None, is_self: bool, mod_note: None, created: int, link_flair_type: AuthorFlairType, wls: int, removed_by_category: None, banned_by: None, author_flair_type: AuthorFlairType, domain: Domain, allow_live_comments: bool, selftext_html: str, likes: None, suggested_sort: Optional[SuggestedSort], banned_at_utc: None, view_count: None, archived: bool, no_follow: bool, is_crosspostable: bool, pinned: bool, over_18: bool, all_awardings: List[Any], awarders: List[Any], media_only: bool, can_gild: bool, spoiler: bool, locked: bool, author_flair_text: Optional[str], treatment_tags: List[Any], visited: bool, removed_by: None, num_reports: None, distinguished: None, subreddit_id: SubredditID, author_is_blocked: bool, mod_reason_by: None, removal_reason: None, link_flair_background_color: str, id: str, is_robot_indexable: bool, report_reasons: None, author: str, discussion_type: None, num_comments: int, send_replies: bool, whitelist_status: WhitelistStatus, contest_mode: bool, mod_reports: List[Any], author_patreon_flair: bool, author_flair_text_color: Optional[FlairTextColor], permalink: str, parent_whitelist_status: WhitelistStatus, stickied: bool, url: str, subreddit_subscribers: int, created_utc: int, num_crossposts: int, media: None, is_video: bool, link_flair_template_id: Optional[UUID]) -> None:
        self.approved_at_utc = approved_at_utc
        self.subreddit = subreddit
        self.selftext = selftext
        self.author_fullname = author_fullname
        self.saved = saved
        self.mod_reason_title = mod_reason_title
        self.gilded = gilded
        self.clicked = clicked
        self.title = title
        self.link_flair_richtext = link_flair_richtext
        self.subreddit_name_prefixed = subreddit_name_prefixed
        self.hidden = hidden
        self.pwls = pwls
        self.link_flair_css_class = link_flair_css_class
        self.downs = downs
        self.thumbnail_height = thumbnail_height
        self.top_awarded_type = top_awarded_type
        self.hide_score = hide_score
        self.name = name
        self.quarantine = quarantine
        self.link_flair_text_color = link_flair_text_color
        self.upvote_ratio = upvote_ratio
        self.author_flair_background_color = author_flair_background_color
        self.subreddit_type = subreddit_type
        self.ups = ups
        self.total_awards_received = total_awards_received
        self.media_embed = media_embed
        self.thumbnail_width = thumbnail_width
        self.author_flair_template_id = author_flair_template_id
        self.is_original_content = is_original_content
        self.user_reports = user_reports
        self.secure_media = secure_media
        self.is_reddit_media_domain = is_reddit_media_domain
        self.is_meta = is_meta
        self.category = category
        self.secure_media_embed = secure_media_embed
        self.link_flair_text = link_flair_text
        self.can_mod_post = can_mod_post
        self.score = score
        self.approved_by = approved_by
        self.is_created_from_ads_ui = is_created_from_ads_ui
        self.author_premium = author_premium
        self.thumbnail = thumbnail
        self.edited = edited
        self.author_flair_css_class = author_flair_css_class
        self.author_flair_richtext = author_flair_richtext
        self.gildings = gildings
        self.content_categories = content_categories
        self.is_self = is_self
        self.mod_note = mod_note
        self.created = created
        self.link_flair_type = link_flair_type
        self.wls = wls
        self.removed_by_category = removed_by_category
        self.banned_by = banned_by
        self.author_flair_type = author_flair_type
        self.domain = domain
        self.allow_live_comments = allow_live_comments
        self.selftext_html = selftext_html
        self.likes = likes
        self.suggested_sort = suggested_sort
        self.banned_at_utc = banned_at_utc
        self.view_count = view_count
        self.archived = archived
        self.no_follow = no_follow
        self.is_crosspostable = is_crosspostable
        self.pinned = pinned
        self.over_18 = over_18
        self.all_awardings = all_awardings
        self.awarders = awarders
        self.media_only = media_only
        self.can_gild = can_gild
        self.spoiler = spoiler
        self.locked = locked
        self.author_flair_text = author_flair_text
        self.treatment_tags = treatment_tags
        self.visited = visited
        self.removed_by = removed_by
        self.num_reports = num_reports
        self.distinguished = distinguished
        self.subreddit_id = subreddit_id
        self.author_is_blocked = author_is_blocked
        self.mod_reason_by = mod_reason_by
        self.removal_reason = removal_reason
        self.link_flair_background_color = link_flair_background_color
        self.id = id
        self.is_robot_indexable = is_robot_indexable
        self.report_reasons = report_reasons
        self.author = author
        self.discussion_type = discussion_type
        self.num_comments = num_comments
        self.send_replies = send_replies
        self.whitelist_status = whitelist_status
        self.contest_mode = contest_mode
        self.mod_reports = mod_reports
        self.author_patreon_flair = author_patreon_flair
        self.author_flair_text_color = author_flair_text_color
        self.permalink = permalink
        self.parent_whitelist_status = parent_whitelist_status
        self.stickied = stickied
        self.url = url
        self.subreddit_subscribers = subreddit_subscribers
        self.created_utc = created_utc
        self.num_crossposts = num_crossposts
        self.media = media
        self.is_video = is_video
        self.link_flair_template_id = link_flair_template_id


class Kind(Enum):
    T3 = "t3"


class PostChild:
    kind: Kind
    data: PostData

    def __init__(self, kind: Kind, data: PostData) -> None:
        self.kind = kind
        self.data = data


class RedditSubredditRestrictedSearchData:
    modhash: str
    dist: int
    facets: Facets
    after: str
    geo_filter: str
    children: List[PostChild]
    before: None

    def __init__(self, modhash: str, dist: int, facets: Facets, after: str, geo_filter: str, children: List[PostChild], before: None) -> None:
        self.modhash = modhash
        self.dist = dist
        self.facets = facets
        self.after = after
        self.geo_filter = geo_filter
        self.children = children
        self.before = before


class RedditSubredditRestrictedSearch:
    kind: str
    data: RedditSubredditRestrictedSearchData

    def __init__(self, kind: str, data: RedditSubredditRestrictedSearchData) -> None:
        self.kind = kind
        self.data = data
