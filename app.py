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


@app.route('/generate_all', methods=['GET'])
def main():
  story = DramatronStory()

  story.title = dramatron.fun_generate_title()
  story.scenes = dramatron.fun_generate_scenes()
  story.places = dramatron.fun_generate_places()
  story.character = dramatron.fun_generate_characters()
  story.story = dramatron.render_story()

  return story

@app.route('/title', methods=['GET'])
def title():
  return dramatron.fun_generate_title()

@app.route('/scenes', methods=['GET'])
def scenes():
  return dramatron.fun_generate_scenes()

@app.route('/places', methods=['GET'])
def places():
  return dramatron.fun_generate_places()

@app.route('/character', methods=['GET'])
def character():
  return dramatron.fun_generate_characters()

@app.route('/story', methods=['GET'])
def story():
  return dramatron.render_story()

if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    port=8080,
    debug=True
  )
