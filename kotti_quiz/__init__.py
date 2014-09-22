from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_quiz')


def includeme(config):

    config.scan(__name__)
    config.add_static_view('static-kotti_quiz', 'kotti_quiz:static')


def kotti_configure(settings):

    settings['kotti.includes'] += ' kotti_quiz'
    settings['kotti.available_types'] += ' kotti_quiz.resources.ContentType'  # noqa
    settings['kotti.fanstatic.view_needed'] += ' kotti_quiz.fanstatic.kotti_quiz_group'  # noqa
