from enum import Enum
from typing import List, Optional, Any


class AdvertiserCategory(Enum):
    EMPTY = ""
    LIFESTYLES = "Lifestyles"
    SPORTS = "Sports"


class AllowedMedia(Enum):
    ANIMATED = "animated"
    EXPRESSION = "expression"
    GIPHY = "giphy"
    STATIC = "static"


class CommentContributionSettings:
    allowed_media_types: Optional[List[AllowedMedia]]

    def __init__(self, allowed_media_types: Optional[List[AllowedMedia]]) -> None:
        self.allowed_media_types = allowed_media_types


class Lang(Enum):
    EN = "en"


class FlairPosition(Enum):
    EMPTY = ""
    LEFT = "left"
    RIGHT = "right"


class SubmissionType(Enum):
    ANY = "any"
    LINK = "link"


class SubredditType(Enum):
    PUBLIC = "public"
    RESTRICTED = "restricted"


class UserFlairType(Enum):
    TEXT = "text"


class WhitelistStatus(Enum):
    ALL_ADS = "all_ads"


class ChildData:
    user_flair_background_color: None
    submit_text_html: Optional[str]
    restrict_posting: bool
    user_is_banned: None
    free_form_reports: bool
    wiki_enabled: bool
    user_is_muted: None
    user_can_flair_in_sr: None
    display_name: str
    header_img: Optional[str]
    title: str
    allow_galleries: bool
    icon_size: Optional[List[int]]
    primary_color: str
    active_user_count: None
    icon_img: str
    display_name_prefixed: str
    accounts_active: None
    public_traffic: bool
    subscribers: int
    user_flair_richtext: List[Any]
    videostream_links_count: Optional[int]
    name: str
    quarantine: bool
    hide_ads: bool
    prediction_leaderboard_entry_type: int
    emojis_enabled: bool
    advertiser_category: AdvertiserCategory
    public_description: str
    comment_score_hide_mins: int
    allow_predictions: bool
    user_has_favorited: None
    user_flair_template_id: None
    community_icon: str
    banner_background_image: str
    original_content_tag_enabled: bool
    community_reviewed: bool
    submit_text: str
    description_html: Optional[str]
    spoilers_enabled: bool
    comment_contribution_settings: CommentContributionSettings
    allow_talks: bool
    header_size: Optional[List[int]]
    user_flair_position: FlairPosition
    all_original_content: bool
    has_menu_widget: bool
    is_enrolled_in_new_modmail: None
    key_color: str
    can_assign_user_flair: bool
    created: int
    wls: Optional[int]
    show_media_preview: bool
    submission_type: SubmissionType
    user_is_subscriber: None
    allowed_media_in_comments: List[AllowedMedia]
    allow_videogifs: bool
    should_archive_posts: bool
    user_flair_type: UserFlairType
    allow_polls: bool
    collapse_deleted_comments: bool
    emojis_custom_size: Optional[List[int]]
    public_description_html: Optional[str]
    allow_videos: bool
    is_crosspostable_subreddit: bool
    suggested_comment_sort: Optional[str]
    should_show_media_in_comments_setting: bool
    can_assign_link_flair: bool
    accounts_active_is_fuzzed: bool
    allow_prediction_contributors: bool
    submit_text_label: str
    link_flair_position: FlairPosition
    user_sr_flair_enabled: None
    user_flair_enabled_in_sr: bool
    allow_discovery: bool
    accept_followers: bool
    user_sr_theme_enabled: bool
    link_flair_enabled: bool
    disable_contributor_requests: bool
    subreddit_type: SubredditType
    notification_level: None
    banner_img: str
    user_flair_text: None
    banner_background_color: str
    show_media: bool
    id: str
    user_is_contributor: None
    over18: bool
    header_title: str
    description: str
    submit_link_label: str
    user_flair_text_color: None
    restrict_commenting: bool
    user_flair_css_class: None
    allow_images: bool
    lang: Lang
    whitelist_status: Optional[WhitelistStatus]
    url: str
    created_utc: int
    banner_size: Optional[List[int]]
    mobile_banner_image: str
    user_is_moderator: None
    allow_predictions_tournament: bool
    content_category: Optional[str]

    def __init__(self, user_flair_background_color: None, submit_text_html: Optional[str], restrict_posting: bool, user_is_banned: None, free_form_reports: bool, wiki_enabled: bool, user_is_muted: None, user_can_flair_in_sr: None, display_name: str, header_img: Optional[str], title: str, allow_galleries: bool, icon_size: Optional[List[int]], primary_color: str, active_user_count: None, icon_img: str, display_name_prefixed: str, accounts_active: None, public_traffic: bool, subscribers: int, user_flair_richtext: List[Any], videostream_links_count: Optional[int], name: str, quarantine: bool, hide_ads: bool, prediction_leaderboard_entry_type: int, emojis_enabled: bool, advertiser_category: AdvertiserCategory, public_description: str, comment_score_hide_mins: int, allow_predictions: bool, user_has_favorited: None, user_flair_template_id: None, community_icon: str, banner_background_image: str, original_content_tag_enabled: bool, community_reviewed: bool, submit_text: str, description_html: Optional[str], spoilers_enabled: bool, comment_contribution_settings: CommentContributionSettings, allow_talks: bool, header_size: Optional[List[int]], user_flair_position: FlairPosition, all_original_content: bool, has_menu_widget: bool, is_enrolled_in_new_modmail: None, key_color: str, can_assign_user_flair: bool, created: int, wls: Optional[int], show_media_preview: bool, submission_type: SubmissionType, user_is_subscriber: None, allowed_media_in_comments: List[AllowedMedia], allow_videogifs: bool, should_archive_posts: bool, user_flair_type: UserFlairType, allow_polls: bool, collapse_deleted_comments: bool, emojis_custom_size: Optional[List[int]], public_description_html: Optional[str], allow_videos: bool, is_crosspostable_subreddit: bool, suggested_comment_sort: Optional[str], should_show_media_in_comments_setting: bool, can_assign_link_flair: bool, accounts_active_is_fuzzed: bool, allow_prediction_contributors: bool, submit_text_label: str, link_flair_position: FlairPosition, user_sr_flair_enabled: None, user_flair_enabled_in_sr: bool, allow_discovery: bool, accept_followers: bool, user_sr_theme_enabled: bool, link_flair_enabled: bool, disable_contributor_requests: bool, subreddit_type: SubredditType, notification_level: None, banner_img: str, user_flair_text: None, banner_background_color: str, show_media: bool, id: str, user_is_contributor: None, over18: bool, header_title: str, description: str, submit_link_label: str, user_flair_text_color: None, restrict_commenting: bool, user_flair_css_class: None, allow_images: bool, lang: Lang, whitelist_status: Optional[WhitelistStatus], url: str, created_utc: int, banner_size: Optional[List[int]], mobile_banner_image: str, user_is_moderator: None, allow_predictions_tournament: bool, content_category: Optional[str]) -> None:
        self.user_flair_background_color = user_flair_background_color
        self.submit_text_html = submit_text_html
        self.restrict_posting = restrict_posting
        self.user_is_banned = user_is_banned
        self.free_form_reports = free_form_reports
        self.wiki_enabled = wiki_enabled
        self.user_is_muted = user_is_muted
        self.user_can_flair_in_sr = user_can_flair_in_sr
        self.display_name = display_name
        self.header_img = header_img
        self.title = title
        self.allow_galleries = allow_galleries
        self.icon_size = icon_size
        self.primary_color = primary_color
        self.active_user_count = active_user_count
        self.icon_img = icon_img
        self.display_name_prefixed = display_name_prefixed
        self.accounts_active = accounts_active
        self.public_traffic = public_traffic
        self.subscribers = subscribers
        self.user_flair_richtext = user_flair_richtext
        self.videostream_links_count = videostream_links_count
        self.name = name
        self.quarantine = quarantine
        self.hide_ads = hide_ads
        self.prediction_leaderboard_entry_type = prediction_leaderboard_entry_type
        self.emojis_enabled = emojis_enabled
        self.advertiser_category = advertiser_category
        self.public_description = public_description
        self.comment_score_hide_mins = comment_score_hide_mins
        self.allow_predictions = allow_predictions
        self.user_has_favorited = user_has_favorited
        self.user_flair_template_id = user_flair_template_id
        self.community_icon = community_icon
        self.banner_background_image = banner_background_image
        self.original_content_tag_enabled = original_content_tag_enabled
        self.community_reviewed = community_reviewed
        self.submit_text = submit_text
        self.description_html = description_html
        self.spoilers_enabled = spoilers_enabled
        self.comment_contribution_settings = comment_contribution_settings
        self.allow_talks = allow_talks
        self.header_size = header_size
        self.user_flair_position = user_flair_position
        self.all_original_content = all_original_content
        self.has_menu_widget = has_menu_widget
        self.is_enrolled_in_new_modmail = is_enrolled_in_new_modmail
        self.key_color = key_color
        self.can_assign_user_flair = can_assign_user_flair
        self.created = created
        self.wls = wls
        self.show_media_preview = show_media_preview
        self.submission_type = submission_type
        self.user_is_subscriber = user_is_subscriber
        self.allowed_media_in_comments = allowed_media_in_comments
        self.allow_videogifs = allow_videogifs
        self.should_archive_posts = should_archive_posts
        self.user_flair_type = user_flair_type
        self.allow_polls = allow_polls
        self.collapse_deleted_comments = collapse_deleted_comments
        self.emojis_custom_size = emojis_custom_size
        self.public_description_html = public_description_html
        self.allow_videos = allow_videos
        self.is_crosspostable_subreddit = is_crosspostable_subreddit
        self.suggested_comment_sort = suggested_comment_sort
        self.should_show_media_in_comments_setting = should_show_media_in_comments_setting
        self.can_assign_link_flair = can_assign_link_flair
        self.accounts_active_is_fuzzed = accounts_active_is_fuzzed
        self.allow_prediction_contributors = allow_prediction_contributors
        self.submit_text_label = submit_text_label
        self.link_flair_position = link_flair_position
        self.user_sr_flair_enabled = user_sr_flair_enabled
        self.user_flair_enabled_in_sr = user_flair_enabled_in_sr
        self.allow_discovery = allow_discovery
        self.accept_followers = accept_followers
        self.user_sr_theme_enabled = user_sr_theme_enabled
        self.link_flair_enabled = link_flair_enabled
        self.disable_contributor_requests = disable_contributor_requests
        self.subreddit_type = subreddit_type
        self.notification_level = notification_level
        self.banner_img = banner_img
        self.user_flair_text = user_flair_text
        self.banner_background_color = banner_background_color
        self.show_media = show_media
        self.id = id
        self.user_is_contributor = user_is_contributor
        self.over18 = over18
        self.header_title = header_title
        self.description = description
        self.submit_link_label = submit_link_label
        self.user_flair_text_color = user_flair_text_color
        self.restrict_commenting = restrict_commenting
        self.user_flair_css_class = user_flair_css_class
        self.allow_images = allow_images
        self.lang = lang
        self.whitelist_status = whitelist_status
        self.url = url
        self.created_utc = created_utc
        self.banner_size = banner_size
        self.mobile_banner_image = mobile_banner_image
        self.user_is_moderator = user_is_moderator
        self.allow_predictions_tournament = allow_predictions_tournament
        self.content_category = content_category


class Kind(Enum):
    T5 = "t5"


class Child:
    kind: Kind
    data: ChildData

    def __init__(self, kind: Kind, data: ChildData) -> None:
        self.kind = kind
        self.data = data


class RedditSubredditSearchData:
    after: str
    dist: int
    modhash: str
    geo_filter: str
    children: List[Child]
    before: None

    def __init__(self, after: str, dist: int, modhash: str, geo_filter: str, children: List[Child], before: None) -> None:
        self.after = after
        self.dist = dist
        self.modhash = modhash
        self.geo_filter = geo_filter
        self.children = children
        self.before = before


class RedditSubredditSearchResult:
    kind: str
    data: RedditSubredditSearchData

    def __init__(self, kind: str, data: RedditSubredditSearchData) -> None:
        self.kind = kind
        self.data = data
