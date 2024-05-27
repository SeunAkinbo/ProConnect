-- Insert categories
INSERT INTO categories (id, name) VALUES
(1, 'Web Development'),
(2, 'Graphic Design'),
(3, 'Data Analysis'),
(4, 'Project Management');

-- Insert profiles for Web Development
INSERT INTO profile (name, description, avatar, email, linkedin, github, address, payment, availability, reviews, category_id)
VALUES
('Alice Johnson', 'Frontend Developer with 5 years of experience.', 'https://i.imgur.com/sSxPe8C.png', 'alice@example.com', 'https://www.linkedin.com/in/alicejohnson', 'https://github.com/alicejohnson', '123 Frontend St, DevCity', 'both', 'remote', 'Highly recommended by peers.', 1),
('Bob Smith', 'Full Stack Developer specializing in JavaScript.', 'https://i.imgur.com/9PGU1BD.png', 'bob@example.com', 'https://www.linkedin.com/in/bobsmith', 'https://github.com/bobsmith', '456 Fullstack Ave, DevTown', 'currency', 'both', 'Excellent problem-solving skills.', 1),
('Charlie Khumalo', 'Backend Developer experienced with Node.js.', 'https://i.imgur.com/OYC8NoC.png', 'charlie@example.com', 'https://www.linkedin.com/in/charliekhumalo', 'https://github.com/charliekhumalo', '789 Backend Blvd, DevCity', 'skill', 'physical', 'Strong backend expertise.', 1);

-- Insert skills for Web Development profiles
INSERT INTO skills (skill_name, duration, profile_id)
VALUES
('HTML - 5 years', 5, 1),
('CSS - 5 years', 5, 1),
('JavaScript - 5 years', 5, 1),
('JavaScript - 6 years', 6, 2),
('Node.js - 4 years', 4, 2),
('React - 3 years', 3, 2),
('Node.js - 4 years', 4, 3),
('Express - 4 years', 4, 3),
('MongoDB - 3 years', 3, 3);

-- Insert profiles for Graphic Design
INSERT INTO profile (name, description, avatar, email, linkedin, github, address, payment, availability, reviews, category_id)
VALUES
('David Green', 'Graphic Designer with a passion for branding.', 'https://i.imgur.com/SQCg0Tg.png', 'david@example.com', 'https://www.linkedin.com/in/davidgreen', 'https://github.com/davidgreen', '101 Design Lane, ArtCity', 'both', 'both', 'Creative and detail-oriented.', 2),
('Eva Zulu', 'Creative designer skilled in Adobe Suite.', 'https://i.imgur.com/jG408z1.png', 'eva@example.com', 'https://www.linkedin.com/in/evazulu', 'https://github.com/evazulu', '202 Design Blvd, ArtTown', 'currency', 'remote', 'Highly innovative designs.', 2),
('Frank Yang', 'Freelance Graphic Designer with 10 years experience.', 'https://i.imgur.com/LBNqwBL.png', 'frank@example.com', 'https://www.linkedin.com/in/frankyang', 'https://github.com/frankyang', '303 Design Ave, ArtCity', 'skill', 'physical', 'Excellent client feedback.', 2);

-- Insert skills for Graphic Design profiles
INSERT INTO skills (skill_name, duration, profile_id)
VALUES
('Photoshop - 7 years', 7, 4),
('Illustrator - 6 years', 6, 4),
('InDesign - 5 years', 5, 4),
('Adobe XD - 4 years', 4, 5),
('Photoshop - 5 years', 5, 5),
('Illustrator - 4 years', 4, 5),
('Logo Design - 10 years', 10, 6),
('Branding - 8 years', 8, 6),
('UI/UX - 6 years', 6, 6);

-- Insert profiles for Data Analysis
INSERT INTO profile (name, description, avatar, email, linkedin, github, address, payment, availability, reviews, category_id)
VALUES
('Grace Okafa', 'Data Analyst specializing in big data.', 'https://i.imgur.com/WOmYx3w.png', 'grace@example.com', 'https://www.linkedin.com/in/graceokafa', 'https://github.com/graceokafa', '404 Data St, TechCity', 'both', 'remote', 'In-depth data analysis skills.', 3),
('Henry Yellow', 'Experienced Data Scientist in Python and R.', 'https://i.imgur.com/dZaQdZQ.png', 'henry@example.com', 'https://www.linkedin.com/in/henryyellow', 'https://github.com/henryyellow', '505 Data Blvd, TechTown', 'currency', 'both', 'Strong analytical skills.', 3),
('James Mabasa', 'Data Engineer with expertise in ETL processes.', 'https://i.imgur.com/4MlH9FP.png', 'james@example.com', 'https://www.linkedin.com/in/ivymabasa', 'https://github.com/jamesmabasa', '606 Data Ave, TechCity', 'skill', 'physical', 'Highly efficient data management.', 3);

-- Insert skills for Data Analysis profiles
INSERT INTO skills (skill_name, duration, profile_id)
VALUES
('Python - 5 years', 5, 7),
('R - 4 years', 4, 7),
('SQL - 6 years', 6, 7),
('Machine Learning - 5 years', 5, 8),
('Data Visualization - 4 years', 4, 8),
('Big Data - 3 years', 3, 8),
('ETL - 5 years', 5, 9),
('Data Warehousing - 4 years', 4, 9),
('SQL - 6 years', 6, 9);

-- Insert profiles for Project Management
INSERT INTO profile (name, description, avatar, email, linkedin, github, address, payment, availability, reviews, category_id)
VALUES
('Alice Wakoko', 'Project manager with a background in software development', 'https://i.imgur.com/PWKhvAw.png', 'alice.wakoko@example.com', 'https://www.linkedin.com/in/alicewakoko', 'https://github.com/alicewakoko', '707 Spruce St, City', 'currency', 'physical', 'Excellent leadership skills', 4),
('Michael King', 'Agile project manager', 'https://i.imgur.com/irwds69.png', 'michael.king@example.com', 'https://www.linkedin.com/in/michaelking', 'https://github.com/michaelking', '808 Fir St, Town', 'skill', 'remote', 'Great with Scrum methodologies', 4),
('Sarah Scott', 'IT project manager', 'https://i.imgur.com/BoR1zOG.png', 'sarah.scott@example.com', 'https://www.linkedin.com/in/sarahscott', 'https://github.com/sarahscott', '909 Ash St, Village', 'both', 'both', 'Strong communication skills', 4);

-- Insert skills for Project Management profiles
INSERT INTO skills (skill_name, duration, profile_id)
VALUES
('Agile - 5 years', 5, 10),
('Scrum - 4 years', 4, 10),
('Kanban - 3 years', 3, 10),
('JIRA - 2 years', 2, 11),
('Confluence - 3 years', 3, 11),
('Trello - 1 year', 1, 11),
('Risk Management - 4 years', 4, 12),
('Budgeting - 3 years', 3, 12),
('Stakeholder Management - 5 years', 5, 12);
