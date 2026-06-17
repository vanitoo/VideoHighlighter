"""
Localization module for VideoHighlighter
Supports English and Russian with auto-detection from system locale.
"""

import locale
import os
import sys
from typing import Dict


# Dictionary of translations
TRANSLATIONS = {
    "en": {
        # Main window title
        "window_title": "Video Highlighter - Highlights & Subtitles",
        
        # File picker section
        "input_videos": "Input Videos",
        "add_videos": "Add Videos",
        "remove_selected": "Remove Selected",
        "clear_all": "Clear All",
        "output_base_name": "Output base name:",
        "output_info": "ℹ️ For multiple files, '_highlight' will be appended to each filename",
        
        # Time range section
        "processing_time_range": "Processing Time Range",
        "process_specific_range": "Process only specific time range",
        "time_range_info": "Set time range in percentages (0-100%) - loads actual times when video is selected",
        "start": "Start:",
        "end": "End",
        "selection_full_video": "Selection: Full video",
        "quick_presets": "Quick presets:",
        "first_5min": "First 5min",
        "last_5min": "Last 5min",
        "last_10min": "Last 10min",
        "middle": "Middle",
        "full_video": "Full video",
        
        # Progress section
        "progress": "Progress",
        "ready": "Ready",
        
        # Download tab
        "download_videos": "Download Videos from Website",
        "page_url": "Page URL:",
        "link_pattern": "Link pattern:",
        "save_directory": "Save directory:",
        "browse": "Browse...",
        "download_time_range": "Download Time Range (Optional)",
        "download_full_video": "Download full video",
        "start_time": "Start time (seconds):",
        "end_time": "End time (seconds):",
        "duration": "Duration:",
        "use_same_time_range": "Use same time range as processing",
        "download_time_info": "ℹ️ Unchecked: Download full videos\n   Checked: Download only selected time range",
        "auto_add_downloaded": "Automatically add downloaded videos to file list",
        "auto_process": "Automatically start processing after download completes",
        "immediate_processing": "Process each video immediately after download",
        "concurrent_downloads": "Concurrent downloads:",
        "download_videos_btn": "🌐 Download Videos",
        "auto_combine": "Automatically combine all highlights into one video",
        "yt_dlp_info": "ℹ️ Requires yt-dlp: pip install yt-dlp",
        
        # Basic Settings tab
        "basic_settings": "Basic Settings",
        "scoring_points": "Scoring Points",
        "scene_points": "Scene points:",
        "motion_event_points": "Motion event points:",
        "motion_peak_points": "Motion peak points:",
        "audio_peak_points": "Audio peak points:",
        "keyword_points": "Keyword points (keywords in transcript):",
        "transcript_points": "Transcript points (all words):",
        "object_points": "Object points:",
        "action_points": "Action points:",
        
        "duration_cutting": "Duration && Cutting",
        "max_highlight_duration": "Max highlight duration (s):",
        "exact_duration": "Exact duration (s, 0 = off):",
        "clip_time": "Clip time (s, 0 = auto):",
        "auto_segmentation": "Auto-Segmentation Settings",
        "min_clip_length": "Min clip length:",
        "max_clip_length": "Max clip length:",
        "merge_gap": "Merge gap:",
        
        "object_detection": "Object detection:",
        "load_labels": "Load Labels",
        "action_keywords": "Action keywords:",
        "actions_require_objects": "Only score actions when objects detected",
        "skip_highlights": "Skip highlights",
        
        # Transcript tab
        "transcript_subtitles": "Transcript && Subtitles",
        "transcript_settings": "Transcript Settings",
        "enable_transcript": "Enable transcript processing",
        "source_language": "Source language:",
        "whisper_model": "Whisper model:",
        "search_keywords": "Search keywords:",
        "subtitle_settings": "Subtitle Settings",
        "create_subtitles": "Create subtitles:",
        
        # Advanced tab
        "advanced": "Advanced",
        "motion_recognition": "Motion Recognition",
        "frame_skip": "Frame skip:",
        "object_recognition": "Object Recognition",
        "yolo_type": "YOLO type:",
        "yolo_model_size": "YOLO model size:",
        "confidence_threshold": "Confidence threshold:",
        "action_recognition": "Action Recognition",
        "backend": "Backend:",
        "models": "Models:",
        "r3d_model_variant": "R3D model variant:",
        "bbox_visualization": "Bounding Box Visualization",
        "draw_object_boxes": "Draw bounding boxes for object detection",
        "draw_action_labels": "Draw labels for action recognition",
        
        # LLM Chat tab
        "llm_chat": "🤖 LLM Chat",
        
        # Avoid tab
        "avoid_people": "🚫 Avoid People",
        "enable_face_recognition": "Enable face recognition",
        "avoid_info": "People you name in the Timeline Viewer (right-click a face → Name) show up here. Tick someone to exclude them from generated highlights.",
        "when_found": "When found:",
        "skip_those_moments": "Skip those moments",
        "crop_them_out": "Crop them out (experimental)",
        "refresh_from_db": "🔄 Refresh from face database",
        "scan_video_faces": "🔍 Scan video for faces",
        "clear_faces": "🗑 Clear faces",
        
        # Controls
        "keep_temp_clips_on": "Keep temp clips: ON",
        "keep_temp_clips_off": "Keep temp clips: OFF",
        "show_timeline": "📊 Show Timeline Viewer",
        "cancel": "Cancel",
        "run_highlighter": "Run Highlighter",
        "log_output": "Log Output:",
        
        # Download tab labels
        "download_tab": "Download",
        
        # Warning dialogs
        "no_analysis_title": "No Analysis Data",
        "no_analysis_msg": "No analysis cache found for this video.\n\nYou can still use the timeline viewer to seek through\nthe video and chat with the LLM — but motion, audio,\nobject and action signals won't be available.\n\nRun the pipeline first to get full signal data.",
        "dont_show_again": "Don't show this warning again",
        "open_anyway": "Open Anyway",
        
        # Label selector
        "filter": "Filter:",
        "labels_available": "labels available",
        "select_all_visible": "Select All Visible",
        "deselect_all": "Deselect All",
        "selected": "selected",
        
        # Status messages
        "starting_download": "🚀 Starting download from:",
        "starting_pipeline": "🚀 Starting video highlighter pipeline...",
        "cancelled": "⏹️ Cancelled",
        "completed": "✅ Completed",
        "error": "❌ Error",
        
        # Timeline viewer
        "signal_timeline": "Signal Timeline",
        "edit_timeline": "Edit Timeline",
        "select_clips_delete": "Select clips and press Delete",
        "drag_to_edit": "Drag signal bars → edit timeline",
        
        # Video preview
        "video_preview": "Video Preview",
        "overlay": "Overlay:",
        "off": "Off",
        "live_cache": "Live (cache)",
        "live_realtime": "Live (real-time)",
        "precomp_swap": "Precomp (swap video)",
        "show_detections": "Show Detections",
        "play": "▶ Play",
        "pause": "⏸ Pause",
        
        # Language settings
        "language": "Language:",
        "auto": "Auto",
        "english": "English",
        "russian": "Русский",
    },
    "ru": {
        # Main window title
        "window_title": "Выделение моментов видео — Субтитры",
        
        # File picker section
        "input_videos": "Входные видео",
        "add_videos": "Добавить видео",
        "remove_selected": "Удалить выбранное",
        "clear_all": "Очистить всё",
        "output_base_name": "Имя выходного файла:",
        "output_info": "ℹ️ Для нескольких файлов будет добавлено '_highlight' к каждому имени",
        
        # Time range section
        "processing_time_range": "Временной диапазон обработки",
        "process_specific_range": "Обрабатывать только определённый диапазон времени",
        "time_range_info": "Установите диапазон в процентах (0-100%) — точные времена загрузятся при выборе видео",
        "start": "Начало:",
        "end": "Конец",
        "selection_full_video": "Выбор: Всё видео",
        "quick_presets": "Быстрые пресеты:",
        "first_5min": "Первые 5 мин",
        "last_5min": "Последние 5 мин",
        "last_10min": "Последние 10 мин",
        "middle": "Середина",
        "full_video": "Всё видео",
        
        # Progress section
        "progress": "Прогресс",
        "ready": "Готово",
        
        # Download tab
        "download_videos": "Загрузка видео с сайта",
        "page_url": "URL страницы:",
        "link_pattern": "Шаблон ссылки:",
        "save_directory": "Папка сохранения:",
        "browse": "Обзор...",
        "download_time_range": "Диапазон загрузки (необязательно)",
        "download_full_video": "Загрузить полное видео",
        "start_time": "Начало (секунды):",
        "end_time": "Конец (секунды):",
        "duration": "Длительность:",
        "use_same_time_range": "Использовать тот же диапазон, что и в обработке",
        "download_time_info": "ℹ️ Выключено: Загрузить полные видео\n   Включено: Загрузить только выбранный диапазон",
        "auto_add_downloaded": "Автоматически добавлять загруженные видео в список",
        "auto_process": "Автоматически начать обработку после загрузки",
        "immediate_processing": "Обрабатывать каждое видео сразу после загрузки",
        "concurrent_downloads": "Одновременные загрузки:",
        "download_videos_btn": "🌐 Загрузить видео",
        "auto_combine": "Автоматически объединить все хайлайты в одно видео",
        "yt_dlp_info": "ℹ️ Требуется yt-dlp: pip install yt-dlp",
        
        # Basic Settings tab
        "basic_settings": "Основные настройки",
        "scoring_points": "Баллы за различные факторы",
        "scene_points": "Баллы за сцены:",
        "motion_event_points": "Баллы за движение:",
        "motion_peak_points": "Баллы за пики движения:",
        "audio_peak_points": "Баллы за звуки:",
        "keyword_points": "Баллы за ключевые слова:",
        "transcript_points": "Баллы за речь:",
        "object_points": "Баллы за объекты:",
        "action_points": "Баллы за действия:",
        
        "duration_cutting": "Длительность && Обрезка",
        "max_highlight_duration": "Макс. длительность хайлайта (сек):",
        "exact_duration": "Точная длительность (сек, 0 = выкл):",
        "clip_time": "Длительность клипа (сек, 0 = авто):",
        "auto_segmentation": "Настройки авто-сегментации",
        "min_clip_length": "Мин. длина клипа:",
        "max_clip_length": "Макс. длина клипа:",
        "merge_gap": "Отступ для объединения:",
        
        "object_detection": "Детекция объектов:",
        "load_labels": "Загрузить метки",
        "action_keywords": "Ключевые слова действий:",
        "actions_require_objects": "Оценивать действия только при обнаружении объектов",
        "skip_highlights": "Пропустить генерацию хайлайтов",
        
        # Transcript tab
        "transcript_subtitles": "Транскрипт && Субтитры",
        "transcript_settings": "Настройки транскрипта",
        "enable_transcript": "Включить обработку транскрипта",
        "source_language": "Исходный язык:",
        "whisper_model": "Модель Whisper:",
        "search_keywords": "Ключевые слова для поиска:",
        "subtitle_settings": "Настройки субтитров",
        "create_subtitles": "Создать субтитры:",
        
        # Advanced tab
        "advanced": "Дополнительно",
        "motion_recognition": "Распознавание движения",
        "frame_skip": "Пропуск кадров:",
        "object_recognition": "Распознавание объектов",
        "yolo_type": "Тип YOLO:",
        "yolo_model_size": "Размер модели YOLO:",
        "confidence_threshold": "Порог уверенности:",
        "action_recognition": "Распознавание действий",
        "backend": "Бэкэнд:",
        "models": "Модели:",
        "r3d_model_variant": "Вариант модели R3D:",
        "bbox_visualization": "Визуализация bounding box",
        "draw_object_boxes": "Рисовать рамки для объектов",
        "draw_action_labels": "Рисовать метки для действий",
        
        # LLM Chat tab
        "llm_chat": "🤖 LLM Чат",
        
        # Avoid tab
        "avoid_people": "🚫 Избегать людей",
        "enable_face_recognition": "Включить распознавание лиц",
        "avoid_info": "Люди, которых вы назвали в Timeline Viewer (правый клик на лице → Имя) появляются здесь. Отметьте кого-то, чтобы исключить из нарезок.",
        "when_found": "При обнаружении:",
        "skip_those_moments": "Пропустить эти моменты",
        "crop_them_out": "Обрезать их (экспериментально)",
        "refresh_from_db": "🔄 Обновить из базы лиц",
        "scan_video_faces": "🔍 Сканировать видео на лица",
        "clear_faces": "🗑 Очистить лица",
        
        # Controls
        "keep_temp_clips_on": "Сохранять временные клипы: ВКЛ",
        "keep_temp_clips_off": "Сохранять временные клипы: ВЫКЛ",
        "show_timeline": "📊 Показать Timeline Viewer",
        "cancel": "Отмена",
        "run_highlighter": "Запустить обработку",
        "log_output": "Журнал:",
        
        # Download tab labels
        "download_tab": "Загрузка",
        
        # Warning dialogs
        "no_analysis_title": "Нет данных анализа",
        "no_analysis_msg": "Для этого видео не найдено кэша анализа.\n\nВы всё ещё можете использовать Timeline Viewer для\nпросмотра видео и общения с LLM, но данные о\nдвижении, звуке, объектах и действиях будут недоступны.\n\nСначала запустите обработку для получения полных данных.",
        "dont_show_again": "Больше не показывать это предупреждение",
        "open_anyway": "Всё равно открыть",
        
        # Label selector
        "filter": "Фильтр:",
        "labels_available": "меток доступно",
        "select_all_visible": "Выбрать все видимые",
        "deselect_all": "Снять все",
        "selected": "выбрано",
        
        # Status messages
        "starting_download": "🚀 Начало загрузки с:",
        "starting_pipeline": "🚀 Запуск конвейера выделения моментов...",
        "cancelled": "⏹️ Отменено",
        "completed": "✅ Завершено",
        "error": "❌ Ошибка",
        
        # Timeline viewer
        "signal_timeline": "Сигналы таймлайна",
        "edit_timeline": "Редактирование таймлайна",
        "select_clips_delete": "Выберите клипы и нажмите Delete",
        "drag_to_edit": "Перетащите полосы сигналов → в редактор",
        
        # Video preview
        "video_preview": "Предпросмотр видео",
        "overlay": "Оверлей:",
        "off": "Выкл",
        "live_cache": "Кэш (live)",
        "live_realtime": "Реал-тайм",
        "precomp_swap": "Заменить видео",
        "show_detections": "Показать обнаружения",
        "play": "▶ Воспроизведение",
        "pause": "⏸ Пауза",
        
        # Language settings
        "language": "Язык:",
        "auto": "Авто",
        "english": "English",
        "russian": "Русский",
    }
}


class Translator:
    """Handles translation with auto-detection of system locale."""
    
    def __init__(self):
        self.current_lang = self._detect_language()
        self.translations = TRANSLATIONS.get(self.current_lang, TRANSLATIONS["en"])
        
    def _detect_language(self) -> str:
        """Detect language from system locale."""
        try:
            # Check environment variable first (for testing)
            env_lang = os.environ.get("VIDEO_HIGHLIGHTER_LANG", "").lower()
            if env_lang in ("ru", "en"):
                return env_lang
            
            # Get system locale
            system_locale = locale.getlocale()[0] or ""
            
            # Check for Russian
            if system_locale and ('ru' in system_locale.lower() or 'rus' in system_locale.lower()):
                return "ru"
                
            # Default to English
            return "en"
        except Exception:
            return "en"
    
    def set_language(self, lang: str):
        """Set translation language explicitly."""
        if lang in TRANSLATIONS:
            self.current_lang = lang
            self.translations = TRANSLATIONS[lang]
            
    def get_current_language(self) -> str:
        """Get current language code."""
        return self.current_lang
    
    def get_language_name(self) -> str:
        """Get display name for current language."""
        if self.current_lang == "ru":
            return "Русский"
        return "English"
    
    def translate(self, key: str) -> str:
        """Translate a string by key."""
        return self.translations.get(key, key)
    
    def get_available_languages(self) -> list:
        """Get list of available languages."""
        return [
            ("en", "English"),
            ("ru", "Русский")
        ]


# Global translator instance
translator = Translator()


def t(key: str) -> str:
    """Shortcut for translation."""
    return translator.translate(key)
