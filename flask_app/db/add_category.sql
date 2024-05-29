-- Insert new categories
INSERT INTO categories (name, field_id) VALUES
-- Technology
('Programming Languages', (SELECT id FROM field WHERE name = 'Technology')),
('Cybersecurity', (SELECT id FROM field WHERE name = 'Technology')),
('Cloud Computing', (SELECT id FROM field WHERE name = 'Technology')),

-- Business
('Marketing', (SELECT id FROM field WHERE name = 'Business')),
('Finance', (SELECT id FROM field WHERE name = 'Business')),
('Sales', (SELECT id FROM field WHERE name = 'Business')),
('Human Resources', (SELECT id FROM field WHERE name = 'Business')),

-- Arts and Humanities
('Writing', (SELECT id FROM field WHERE name = 'Arts and Humanities')),
('Performing Arts', (SELECT id FROM field WHERE name = 'Arts and Humanities')),
('Languages', (SELECT id FROM field WHERE name = 'Arts and Humanities')),
('History and Culture', (SELECT id FROM field WHERE name = 'Arts and Humanities')),

-- Sciences
('Biology', (SELECT id FROM field WHERE name = 'Sciences')),
('Chemistry', (SELECT id FROM field WHERE name = 'Sciences')),
('Physics', (SELECT id FROM field WHERE name = 'Sciences')),
('Environmental Science', (SELECT id FROM field WHERE name = 'Sciences')),
('Mathematics', (SELECT id FROM field WHERE name = 'Sciences')),

-- Healthcare
('Clinical Skills', (SELECT id FROM field WHERE name = 'Healthcare')),
('Nursing', (SELECT id FROM field WHERE name = 'Healthcare')),
('Public Health', (SELECT id FROM field WHERE name = 'Healthcare')),
('Mental Health', (SELECT id FROM field WHERE name = 'Healthcare')),
('Pharmacy', (SELECT id FROM field WHERE name = 'Healthcare')),

-- Education
('Teaching', (SELECT id FROM field WHERE name = 'Education')),
('Training', (SELECT id FROM field WHERE name = 'Education')),
('Research', (SELECT id FROM field WHERE name = 'Education')),
('Language Teaching', (SELECT id FROM field WHERE name = 'Education')),
('Educational Administration', (SELECT id FROM field WHERE name = 'Education')),

-- Trades and Crafts
('Construction', (SELECT id FROM field WHERE name = 'Trades and Crafts')),
('Automotive', (SELECT id FROM field WHERE name = 'Trades and Crafts')),
('Culinary Arts', (SELECT id FROM field WHERE name = 'Trades and Crafts')),
('Fashion Design', (SELECT id FROM field WHERE name = 'Trades and Crafts')),
('Woodworking', (SELECT id FROM field WHERE name = 'Trades and Crafts')),

-- Engineering
('Mechanical Engineering', (SELECT id FROM field WHERE name = 'Engineering')),
('Civil Engineering', (SELECT id FROM field WHERE name = 'Engineering')),
('Electrical Engineering', (SELECT id FROM field WHERE name = 'Engineering')),
('Chemical Engineering', (SELECT id FROM field WHERE name = 'Engineering')),
('Software Engineering', (SELECT id FROM field WHERE name = 'Engineering')),

-- Agriculture
('Crop Management', (SELECT id FROM field WHERE name = 'Agriculture')),
('Animal Husbandry', (SELECT id FROM field WHERE name = 'Agriculture')),
('Agricultural Technology', (SELECT id FROM field WHERE name = 'Agriculture')),
('Horticulture', (SELECT id FROM field WHERE name = 'Agriculture')),
('Agribusiness', (SELECT id FROM field WHERE name = 'Agriculture')),

-- Environmental Science and Sustainability
('Environmental Engineering', (SELECT id FROM field WHERE name = 'Environmental Science and Sustainability')),
('Sustainability', (SELECT id FROM field WHERE name = 'Environmental Science and Sustainability')),
('Conservation', (SELECT id FROM field WHERE name = 'Environmental Science and Sustainability')),
('Geology', (SELECT id FROM field WHERE name = 'Environmental Science and Sustainability')),
('Marine Biology', (SELECT id FROM field WHERE name = 'Environmental Science and Sustainability')),

-- Social Sciences
('Psychology', (SELECT id FROM field WHERE name = 'Social Sciences')),
('Sociology', (SELECT id FROM field WHERE name = 'Social Sciences')),
('Political Science', (SELECT id FROM field WHERE name = 'Social Sciences')),
('Economics', (SELECT id FROM field WHERE name = 'Social Sciences')),
('Anthropology', (SELECT id FROM field WHERE name = 'Social Sciences')),

-- Law and Legal Studies
('Legal Research', (SELECT id FROM field WHERE name = 'Law and Legal Studies')),
('Corporate Law', (SELECT id FROM field WHERE name = 'Law and Legal Studies')),
('Criminal Law', (SELECT id FROM field WHERE name = 'Law and Legal Studies')),
('International Law', (SELECT id FROM field WHERE name = 'Law and Legal Studies')),
('Environmental Law', (SELECT id FROM field WHERE name = 'Law and Legal Studies')),

-- Media and Communication
('Journalism', (SELECT id FROM field WHERE name = 'Media and Communication')),
('Public Relations', (SELECT id FROM field WHERE name = 'Media and Communication')),
('Film and Video Production', (SELECT id FROM field WHERE name = 'Media and Communication')),
('Advertising', (SELECT id FROM field WHERE name = 'Media and Communication')),

-- Sports and Recreation
('Coaching', (SELECT id FROM field WHERE name = 'Sports and Recreation')),
('Fitness Training', (SELECT id FROM field WHERE name = 'Sports and Recreation')),
('Outdoor Education', (SELECT id FROM field WHERE name = 'Sports and Recreation')),
('Sports Medicine', (SELECT id FROM field WHERE name = 'Sports and Recreation')),
('Event Management', (SELECT id FROM field WHERE name = 'Sports and Recreation')),

-- Hospitality and Tourism
('Hotel Management', (SELECT id FROM field WHERE name = 'Hospitality and Tourism')),
('Event Planning', (SELECT id FROM field WHERE name = 'Hospitality and Tourism')),
('Travel and Tourism', (SELECT id FROM field WHERE name = 'Hospitality and Tourism')),
('Restaurant Management', (SELECT id FROM field WHERE name = 'Hospitality and Tourism')),

-- Logistics and Supply Chain
('Supply Chain Management', (SELECT id FROM field WHERE name = 'Logistics and Supply Chain')),
('Logistics', (SELECT id FROM field WHERE name = 'Logistics and Supply Chain')),
('Operations Management', (SELECT id FROM field WHERE name = 'Logistics and Supply Chain')),
('Distribution', (SELECT id FROM field WHERE name = 'Logistics and Supply Chain')),
('E-commerce Logistics', (SELECT id FROM field WHERE name = 'Logistics and Supply Chain')),

-- Design and Architecture
('Interior Design', (SELECT id FROM field WHERE name = 'Design and Architecture')),
('Architecture', (SELECT id FROM field WHERE name = 'Design and Architecture')),
('Landscape Architecture', (SELECT id FROM field WHERE name = 'Design and Architecture')),
('Industrial Design', (SELECT id FROM field WHERE name = 'Design and Architecture')),

-- Public Service and Safety
('Emergency Management', (SELECT id FROM field WHERE name = 'Public Service and Safety')),
('Firefighting', (SELECT id FROM field WHERE name = 'Public Service and Safety')),
('Law Enforcement', (SELECT id FROM field WHERE name = 'Public Service and Safety')),
('Public Administration', (SELECT id FROM field WHERE name = 'Public Service and Safety')),
('Military Skills', (SELECT id FROM field WHERE name = 'Public Service and Safety')),

-- Information Technology
('IT Support', (SELECT id FROM field WHERE name = 'Information Technology')),
('Database Management', (SELECT id FROM field WHERE name = 'Information Technology')),
('Network Administration', (SELECT id FROM field WHERE name = 'Information Technology')),
('System Architecture', (SELECT id FROM field WHERE name = 'Information Technology'));
