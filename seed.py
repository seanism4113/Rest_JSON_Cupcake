from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://sallysbakingaddiction.com/wp-content/uploads/2017/06/moist-chocolate-cupcakes-5.jpg"
)

c3 = Cupcake(
    flavor="cookies & cream",
    size="large",
    rating=10,
    image="https://laneandgreyfare.com/wp-content/uploads/2023/07/Cookies-and-Cream-Cupcakes-1.jpg"
)

c4 = Cupcake(
    flavor="vanilla",
    size="medium",
    rating=3,
    image="https://www.ifyougiveablondeakitchen.com/wp-content/uploads/2017/03/vanilla-cupcakes-open-graph-image-500x500.jpg"
)

db.session.add_all([c1, c2, c3, c4])
db.session.commit()

