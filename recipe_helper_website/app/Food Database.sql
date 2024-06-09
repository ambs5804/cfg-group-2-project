CREATE DATABASE SUBSTITUTIONS;

CREATE TABLE vegan_alternatives (
original_ingredient VARCHAR(100),
quantity integer,
subbed_ingredient VARCHAR (100),
subbed_quantity integer
);

-- INSERT INTO vegan_alternatives (original_ingredient, quantity, subbed_ingredient, subbed_quantity)
VALUES ('cows milk', 50, 'oat milk', 50),
('dairy_butter',50,'margerine',50);

DROP TABLE vegan_alternatives;

CREATE TABLE FoodItems(
Food_ID INTEGER,
Food_Name VARCHAR(100),
Category VARCHAR(100),
Quantity INTEGER
);

ALTER TABLE FoodItems
ADD PRIMARY KEY (Food_ID);

ALTER TABLE FoodItems
MODIFY COLUMN Food_ID INT NOT NULL AUTO_INCREMENT;

CREATE TABLE Alternatives (
    Food_ID INTEGER NOT NULL,
    Alternative_Food_ID INTEGER NOT NULL,
    FOREIGN KEY (Food_ID) REFERENCES FoodItems(Food_ID),
    FOREIGN KEY (Alternative_Food_ID) REFERENCES FoodItems(Food_ID),
    PRIMARY KEY (Food_ID, Alternative_Food_ID)
);

ALTER TABLE FoodItems
MODIFY COLUMN quantity VARCHAR(100);

INSERT INTO FoodItems (Food_Name, Category, Quantity)
VALUES ('Dairy Milk', 'Dairy', '100ml'),
('Oat Milk', 'Plant Based', '100ml'),
('Almond Milk','Plant Based', '100ml'),
('Soya Milk', 'Plant Based', '100ml'),
('Coconut Milk', 'Plant Based', '100ml'),
('Egg', 'Non-vegan Ingredient', '1 unit'),
('Aquafaba', 'Plant Based', '3 tablespoons'),
('Egg Replacement', 'Plant Based', '1 tablespoon'),
('Dairy Butter', 'Dairy', '100g'),
('Plant Based Butter', 'Plant Based', '100g'),
('Margerine', 'Plant Based', '100g'),
('Cheese','Dairy','50g'),
('Plant Based Cheese', 'Plant Based', '50g'),
('Nutritional Yeast', 'Plant Based','1 tablespoon'),
('Honey', 'Animal Product', '1 tablespoon'),
('Maple Syrup', 'Plant Based', '1 tablespoon'),
('Agave Syrup', 'Plant Based', '1 tablespoon'),
('Egg Mayonaise', 'Animal Product', '50g'),
('Vegan Mayonaise', 'Plant Based', '50g'),
('Meat', 'Animal Product', '100g'),
('Tofu', 'Plant Based', '100g'),
('Seitan','Plant Based', '100g'),
('Tempeh', 'Plant Based', '100g'),
('TVP', 'Plant Based', '100g'),
('Arrowroot starch', 'Plant Based', '1 teaspoon'),
('All purpose flour', 'Plant Based', '1 tablespoon'),
('Cornstarch','Plant Based', '1 teaspoon'),
('Broth (Beef/Chicken)','Animal Product', '100ml'),
('Bouillon Cube','Plant Based', '1 unit'),
('Vegetable Broth', 'Plant Based', '100ml'),
('Herbs (fresh)', 'Plant Based', '1 tablespoon'),
('Herbs (dried)', 'Plant Based', '1 teaspoon'),
('Lime Juice', 'Plant Based', '1 teaspoon'),
('Vinegar', 'Plant Based', '1 teaspoon'),
('White Wine', 'Plant Based', '1 teaspoon'),
('Baking Soda', 'Plant Based', '1 teaspoon'),
('Baking Powder', 'Plant Based', '4 teaspoons');

SELECT * FROM FoodItems

INSERT INTO Alternatives (Food_ID, Alternative_Food_ID)
VALUES (1,2),
(1,3),
(1,4),
(1,5),
(6,7),
(6,8),
(9,10),
(9,11),
(12,13),
(12,14),
(15,16),
(15,17),
(18,19),
(20,21),
(20,22),
(20,23),
(20,24),
(25,26),
(25,27),
(28,29),
(28,30),
(31,32),
(33,34),
(33,35),
(36,37);


SELECT 
    fi.Food_Name AS Original_Ingredient, 
    fa.Food_Name AS Alternative_Ingredient
FROM 
    Alternatives a
JOIN 
    FoodItems fi ON a.Food_ID = fi.Food_ID
JOIN 
    FoodItems fa ON a.Alternative_Food_ID = fa.Food_ID;
