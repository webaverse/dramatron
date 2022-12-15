from typing import NamedTuple
import dramatron

from flask import Flask


app = Flask(__name__)


class DramatronStory(NamedTuple):
  title: str
  scenes: str
  places: str
  character: str
  story: str


@app.route('/')
def main():
  story = DramatronStory()

  story.title = dramatron.fun_generate_title()
  story.scenes = dramatron.fun_generate_scenes()
  story.places = dramatron.fun_generate_places()
  story.character = dramatron.fun_generate_characters()
  story.story = dramatron.render_story()

  return story


if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    port=8080,
    debug=True
  )
