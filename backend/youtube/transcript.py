from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()

def get_transcript(video_id):

    transcript = api.fetch(video_id)

    text ="".join(snippet.text for snippet in transcript)

    return text