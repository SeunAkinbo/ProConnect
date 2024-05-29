-- Create the tables
CREATE TABLE field (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE category (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    field_id INT,
    FOREIGN KEY (field_id) REFERENCES field(id)
);

-- Insert into field table
INSERT INTO field (id, name) VALUES
(1, 'Technology'),
(2, 'Business'),
(3, 'Arts and Humanities'),
(4, 'Sciences'),
(5, 'Healthcare'),
(6, 'Education'),
(7, 'Trades and Crafts'),
(8, 'Engineering'),
(9, 'Agriculture'),
(10, 'Environmental Science and Sustainability'),
(11, 'Social Sciences'),
(12, 'Law and Legal Studies'),
(13, 'Media and Communication'),
(14, 'Sports and Recreation'),
(15, 'Hospitality and Tourism'),
(16, 'Logistics and Supply Chain'),
(17, 'Design and Architecture'),
(18, 'Public Service and Safety'),
(19, 'Information Technology');

-- Insert into category table
INSERT INTO category (id, name, field_id) VALUES
-- Technology
(1, 'Programming Languages', 1),
(2, 'Web Development', 1),
(3, 'Data Analysis', 1),
(4, 'Cybersecurity', 1),
(5, 'Cloud Computing', 1),

-- Business
(6, 'Project Management', 2),
(7, 'Marketing', 2),
(8, 'Finance', 2),
(9, 'Sales', 2),
(10, 'Human Resources', 2),

-- Arts and Humanities
(11, 'Writing', 3),
(12, 'Graphic Design', 3),
(13, 'Performing Arts', 3),
(14, 'Languages', 3),
(15, 'History and Culture', 3),

-- Sciences
(16, 'Biology', 4),
(17, 'Chemistry', 4),
(18, 'Physics', 4),
(19, 'Environmental Science', 4),
(20, 'Mathematics', 4),

-- Healthcare
(21, 'Clinical Skills', 5),
(22, 'Nursing', 5),
(23, 'Public Health', 5),
(24, 'Mental Health', 5),
(25, 'Pharmacy', 5),

-- Education
(26, 'Teaching', 6),
(27, 'Training', 6),
(28, 'Research', 6),
(29, 'Language Teaching', 6),
(30, 'Educational Administration', 6),

-- Trades and Crafts
(31, 'Construction', 7),
(32, 'Automotive', 7),
(33, 'Culinary Arts', 7),
(34, 'Fashion Design', 7),
(35, 'Woodworking', 7),

-- Engineering
(36, 'Mechanical Engineering', 8),
(37, 'Civil Engineering', 8),
(38, 'Electrical Engineering', 8),
(39, 'Chemical Engineering', 8),
(40, 'Software Engineering', 8),

-- Agriculture
(41, 'Crop Management', 9),
(42, 'Animal Husbandry', 9),
(43, 'Agricultural Technology', 9),
(44, 'Horticulture', 9),
(45, 'Agribusiness', 9),

-- Environmental Science and Sustainability
(46, 'Environmental Engineering', 10),
(47, 'Sustainability', 10),
(48, 'Conservation', 10),
(49, 'Geology', 10),
(50, 'Marine Biology', 10),

-- Social Sciences
(51, 'Psychology', 11),
(52, 'Sociology', 11),
(53, 'Political Science', 11),
(54, 'Economics', 11),
(55, 'Anthropology', 11),

-- Law and Legal Studies
(56, 'Legal Research', 12),
(57, 'Corporate Law', 12),
(58, 'Criminal Law', 12),
(59, 'International Law', 12),
(60, 'Environmental Law', 12),

-- Media and Communication
(61, 'Journalism', 13),
(62, 'Public Relations', 13),
(63, 'Film and Video Production', 13),
(64, 'Graphic Design', 13),
(65, 'Advertising', 13),

-- Sports and Recreation
(66, 'Coaching', 14),
(67, 'Fitness Training', 14),
(68, 'Outdoor Education', 14),
(69, 'Sports Medicine', 14),
(70, 'Event Management', 14),

-- Hospitality and Tourism
(71, 'Hotel Management', 15),
(72, 'Culinary Arts', 15),
(73, 'Event Planning', 15),
(74, 'Travel and Tourism', 15),
(75, 'Restaurant Management', 15),

-- Logistics and Supply Chain
(76, 'Supply Chain Management', 16),
(77, 'Logistics', 16),
(78, 'Operations Management', 16),
(79, 'Distribution', 16),
(80, 'E-commerce Logistics', 16),

-- Design and Architecture
(81, 'Interior Design', 17),
(82, 'Architecture', 17),
(83, 'Landscape Architecture', 17),
(84, 'Fashion Design', 17),
(85, 'Industrial Design', 17),

-- Public Service and Safety
(86, 'Emergency Management', 18),
(87, 'Firefighting', 18),
(88, 'Law Enforcement', 18),
(89, 'Public Administration', 18),
(90, 'Military Skills', 18),

-- Information Technology
(91, 'IT Support', 19),
(92, 'Database Management', 19),
(93, 'Network Administration', 19),
(94, 'System Architecture', 19),
(95, 'Cybersecurity', 19);
