
from flask import Flask, render_template, request

app = Flask(__name__)

artists = [
    {
        'id': 1,
        'name': 'John Doe',
        'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget lacus eget nunc tincidunt laoreet. Integer eget lectus eget nunc tincidunt laoreet.',
        'portfolio': ['image1.jpg', 'image2.jpg', 'image3.jpg'],
        'social_media': ['twitter.com/johndoe', 'instagram.com/johndoe', 'facebook.com/johndoe']
    },
    {
        'id': 2,
        'name': 'Jane Doe',
        'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget lacus eget nunc tincidunt laoreet. Integer eget lectus eget nunc tincidunt laoreet.',
        'portfolio': ['image4.jpg', 'image5.jpg', 'image6.jpg'],
        'social_media': ['twitter.com/janedoe', 'instagram.com/janedoe', 'facebook.com/janedoe']
    }
]

collaborations = [
    {
        'id': 1,
        'title': 'Project 1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget lacus eget nunc tincidunt laoreet. Integer eget lectus eget nunc tincidunt laoreet.',
        'participants': ['John Doe', 'Jane Doe'],
        'gallery': ['image1.jpg', 'image2.jpg', 'image3.jpg']
    },
    {
        'id': 2,
        'title': 'Project 2',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget lacus eget nunc tincidunt laoreet. Integer eget lectus eget nunc tincidunt laoreet.',
        'participants': ['John Doe', 'Jane Doe'],
        'gallery': ['image4.jpg', 'image5.jpg', 'image6.jpg']
    }
]

@app.route('/')
def index():
    return render_template('index.html', artists=artists, collaborations=collaborations)

@app.route('/artist/<artist_id>')
def artist_detail(artist_id):
    artist = next((artist for artist in artists if artist['id'] == int(artist_id)), None)
    return render_template('artist-detail.html', artist=artist)

@app.route('/upload-artwork', methods=['POST'])
def upload_artwork():
    if request.method == 'POST':
        # Save the uploaded artwork to the platform
        pass
    return render_template('upload-artwork.html')

@app.route('/create-collaboration', methods=['POST'])
def create_collaboration():
    if request.method == 'POST':
        # Create a new collaboration project and send invitations to the specified participants
        pass
    return render_template('create-collaboration.html')

@app.route('/collaboration/<collaboration_id>')
def collaboration_detail(collaboration_id):
    collaboration = next((collaboration for collaboration in collaborations if collaboration['id'] == int(collaboration_id)), None)
    return render_template('collaboration-detail.html', collaboration=collaboration)

if __name__ == '__main__':
    app.run()
