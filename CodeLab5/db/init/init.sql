CREATE TABLE IF NOT EXISTS Meals (
    MealId SERIAL PRIMARY KEY
    ,MealName TEXT NOT NULL
    ,MealPrice REAL NOT NULL
);

INSERT INTO Meals(MealName, MealPrice) VALUES ('Baked Lasagna', 14.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Chicken Marsala', 16.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Fiorillo House Salad', 18.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Pasta Romano', 12.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Fried Calamari', 17.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Sun-dried Tomato and Basil', 12.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Cannoli', 10.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Cheese Chilly Toast', 13.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Penne Pasta', 14.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Krusty Popcorn', 18.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Bruschetta', 12.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Tiramisu', 12.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Baked Beans on Bread', 13.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Chocolate Cheesecake', 8.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Raspberry Cheesecake', 8.99);

