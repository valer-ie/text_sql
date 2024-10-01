import sqlite3

## Connect to sqlite
connection = sqlite3.connect("film.db")

## Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()


table_info = """
CREATE TABLE film (
  filmID INT,
  title VARCHAR(255) NOT NULL,
  description varchar(1000),
  releaseYear SMALLINT,
  length SMALLINT UNSIGNED,
  replacementCost DECIMAL(5,2) NOT NULL DEFAULT 19.99,
  rating VARCHAR(5) NOT NULL,
  CONSTRAINT film_pk PRIMARY KEY (filmID),
  CONSTRAINT film_replacementCost_ck CHECK (replacementCost > 9.99)
);
"""

cursor.execute(table_info)

'''
-- ISTE-230 Version 2 - modified by David Patric and Elissa Weeden, 6/2020

-- Sakila Sample Database Schema
-- Version 0.8

-- Copyright (c) 2006, MySQL AB
-- All rights reserved.

-- Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

--  * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
--  * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
--  * Neither the name of MySQL AB nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

-- THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-- ----------------------------------------------------------------------------------
'''



cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (1,'ACADEMY DINOSAUR','An Epic Drama of a Feminist And a Mad Scientist who must Save a Teacher in The Canadian Rockies',2006,86,20.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (2,'ACE GOLDFINGER','An Astounding story of a Database Administrator And a Explorer who must Find a Car in Ancient China',2007,48,12.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (3,'ADAPTATION','A Astounding Reflection of a Lumberjack And a Car who must Sink a Lumberjack in A Baloon Factory',2008,50,18.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (4,'A FAIR RACE','A Fanciful Documentary of a Frisbee And a Lumberjack who must Chase a Monkey in A Shark Tank',2009,117,26.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (5,'AFRICAN EGG','A Fast-Paced Documentary of a Pastry Chef And a Dentist who must Find a Forensic Psychologist in The Gulf of Mexico',2006,130,22.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (6,'AGENT TRUMAN','A Intrepid Panorama of a Robot And a Boy who must Escape a Sumo Wrestler in Ancient China',2010,169,17.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (7,'AIRPLANE SIERRA','A Saga of a Hunter And a Butler who must Find a Kidnapped Butler in A Jet Boat',2011,62,28.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (8,'BALLOON HOMEWARD','A Insightful Panorama of a Forensic Psychologist And a Mad Cow who must Build a Mad Scientist in The First Manned Space Station',2007,75,10.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (9,'BALLROOM MOCKINGBIRD','A Thrilling Documentary of a Composer And a Monkey who must Find a Feminist in California',2008,173,29.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (10,'BAN FANG','A Epic Drama of a Madman And a Cat who must Face a A Shark in An Abandoned Amusement Park',2009,87,25.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (11,'BOY PINOCCHIO','A Awe-Inspiring Drama of a Car And a Pastry Chef who must Chase a Crocodile in The First Manned Space Station',2010,113,15.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (12,'BARBARELLA STREETCAR','A Awe-Inspiring Story of a Feminist And a Cat who must Help a Dog in A Monastery',2011,65,27.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (13,'BAREFOOT MANCHURIAN','A Intrepid Story of a Cat And a Student who must Rescue a Girl in An Abandoned Amusement Park',2012,129,15.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (14,'BASIC EASY','A Stunning story of a Man And a Husband who must Reach a Mad Scientist in A Jet Boat',2013,90,18.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (15,'BEACH HEARTBREAKERS','A Fateful Display of a Athlete And a Mad Scientist who must Outrun a A Shark in Georgia',2006,122,16.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (16,'BEAR GRACELAND','A Astounding Saga of a Dog And a Boy who must Join a Teacher in The First Manned Space Station',2007,160,20.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (17,'BEAST HUNCHBACK',NULL,2008,89,22.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (18,'CASUALTIES ENCINO','A Insightful Yarn of a A Shark And a Pastry Chef who must Face a Boy in A Monastery',2010,179,16.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (19,'CAT CONEHEADS','A Fast-Paced Panorama of a Girl And a A Shark who must Confront a Boy in Ancient India',2011,112,14.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (20,'CATCH AMISTAD','A Boring Reflection of a Lumberjack And a Feminist who must Find a Woman in Nigeria',2012,183,10.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (21,'CAUSE DATE','A Taut Tale of a Explorer And a Pastry Chef who must Help a Hunter in A MySQL Convention',2013,179,16.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (22,'CELEBRITY HORN','A Amazing Documentary of a Secret Agent And a Astronaut who must Vanquish a Hunter in A Shark Tank',2006,110,24.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (23,'CONVERSATION DOWNHILL','A Taut Character Study of a Husband And a Waitress who must Sink a Squirrel in A MySQL Convention',2009,112,14.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (24,'CORE SUIT','A Unbelieveable Tale of a Car And a Explorer who must Confront a Boat in A Manhattan Penthouse',2010,92,24.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (25,'COWBOY DOOM','A Astounding Drama of a Boy And a Lumberjack who must Rescue a Butler in A Baloon',2011,146,10.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (26,'CRAFT OUTFIELD','A Lacklusture Display of a Explorer And a Hunter who must Outsmart a Database Administrator in A Baloon Factory',2012,64,17.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (27,'CRANES RESERVOIR','A Fanciful Documentary of a Teacher And a Dog who must Outrun a Forensic Psychologist in A Baloon Factory',2013,57,12.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (28,'CRAZY HOME','A Fanciful Panorama of a Boy And a Woman who must Vanquish a Database Administrator in The Outback',2006,136,24.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (29,'CREATURES SHAKESPEARE','A Emotional Drama of a Athlete And a Squirrel who must Vanquish a Crocodile in Ancient India',2007,139,23.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (30,'CREEPERS KANE','A Awe-Inspiring Reflection of a Squirrel And a Boat who must Outrace a Car in A Jet Boat',2008,172,23.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (31,'CROOKED FROGMEN','A Unbelieveable Drama of a Hunter And a Database Administrator who must Save a Crocodile in An Abandoned Amusement Park',2009,143,27.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (32,'EARTH VISION','A Stunning Drama of a Butler And a Madman who must Outrace a Athlete in Ancient India',2007,85,29.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (33,'EASY GLADIATOR','A Fateful Story of a Monkey And a Girl who must Outwit a Pastry Chef in Ancient India',2008,148,12.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (34,'EDGE RUNNER','A Beautiful Yarn of a Composer And a Mad Cow who must Redeem a Mad Scientist in A Jet Boat',2009,153,19.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (35,'EFFECT GLADIATOR','A Beautiful Display of a Pastry Chef And a Pastry Chef who must Outrun a Forensic Psychologist in A Manhattan Penthouse',2010,107,14.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (36,'EGG IGBY','A Beautiful Documentary of a Boat And a Sumo Wrestler who must Outsmart a Database Administrator in The First Manned Space Station',2011,67,20.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (37,'EGYPT TENENBAUMS','A Intrepid Story of a Madman And a Secret Agent who must Outrace a Astronaut in An Abandoned Amusement Park',2012,85,11.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (38,'ELEMENT FREDDY','A Awe-Inspiring Reflection of a Waitress And a Squirrel who must Defeat a Mad Cow in A Jet Boat',2013,115,28.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (39,'ELEPHANT TROY','A Beautiful Panorama of a Lumberjack And a Forensic Psychologist who must Outwit a Frisbee in A Baloon',2006,126,24.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (40,'ELF MURDER','A Action-Packed Story of a Frisbee And a Woman who must Reach a Girl in An Abandoned Mine Shaft',2007,155,19.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (41,'GHOST GROUNDHOG','A Brilliant Panorama of a Madman And a Composer who must Outsmart a Car in Ancient India',2013,85,18.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (42,'GHOSTBUSTERS ELF','A Thoughtful story of a Dog And a Feminist who must Chase a Composer in Berlin',2006,101,18.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (43,'GIANT TROOPERS','A Fateful Display of a Feminist And a Monkey who must Vanquish a Monkey in The Canadian Rockies',2007,102,10.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (44,'GILBERT PELICAN','A Fateful Tale of a Man And a Feminist who must Help a Crocodile in A Manhattan Penthouse',2008,114,13.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (45,'GILMORE BOILED','A Unbelieveable Documentary of a Boat And a Husband who must Outsmart a Student in A Submarine',2009,163,29.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (46,'GLADIATOR WESTWARD','A Astounding Reflection of a Squirrel And a Sumo Wrestler who must Sink a Dentist in Ancient Japan',2010,173,20.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (47,'GLASS DYING','A Astounding Drama of a Frisbee And a Astronaut who must Rescue a Dog in Ancient Japan',2011,103,24.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (48,'GLEAMING JAWBREAKER','A Amazing Display of a Composer And a Forensic Psychologist who must Discover a Car in The Canadian Rockies',2012,89,25.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (49,'GLORY TRACY','A Amazing Saga of a Woman And a Athlete who must Discover a Cat in The First Manned Space Station',2013,115,13.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (50,'GO PURPLE','A Fast-Paced Display of a Car And a Database Administrator who must Save a Woman in A Baloon',2006,54,12.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (51,'SUPER WYOMING','A Action-Packed Saga of a Pastry Chef And a Explorer who must Discover a A Shark in The Outback',2009,58,10.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (52,'SUPERFLY TRIP','A Beautiful Saga of a Lumberjack And a Teacher who must Build a Technical Writer in An Abandoned Fun House',2010,114,27.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (53,'SUSPECTS QUILLS','A Emotional story of a Pioneer And a Crocodile who must Save a Man in A Manhattan Penthouse',2011,47,22.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (54,'SWARM GOLD','A Insightful Panorama of a Crocodile And a Boat who must Help a Sumo Wrestler in A MySQL Convention',2012,123,12.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (55,'SWEDEN SHINING','A Taut Documentary of a Car And a Robot who must Help a Boy in The Canadian Rockies',2013,176,19.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (56,'SWEET BROTHERHOOD','A Unbelieveable story of a Sumo Wrestler And a Hunter who must Chase a Forensic Psychologist in A Baloon',2006,185,27.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (57,'SWEETHEARTS SUSPECTS','A Brilliant Character Study of a Frisbee And a Sumo Wrestler who must Confront a Woman in The Gulf of Mexico',2007,108,13.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (58,'TADPOLE PARK','A Beautiful Tale of a Frisbee And a Moose who must Vanquish a Dog in An Abandoned Amusement Park',2008,155,13.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (59,'TALENTED TANK','A Lacklusture Panorama of a Dentist And a Forensic Psychologist who must Outrace a Pioneer in A Submarine',2009,173,19.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (60,'TARZAN VIDEOTAPE','A Fast-Paced Display of a Lumberjack And a Mad Scientist who must Outsmart a Sumo Wrestler in The Sahara Desert',2010,91,11.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (61,'TAXI KICK','A Amazing story of a Girl And a Woman who must Outrace a Waitress in Georgia',2011,64,23.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (62,'TEEN APOLLO','A Awe-Inspiring Drama of a Dog And a Man who must Escape a Robot in A Shark Tank',2012,74,25.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (63,'TELEGRAPH VOYAGE','A Fateful Yarn of a Husband And a Dog who must Save a Waitress in A Jet Boat',2013,148,20.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (64,'TELEMARK HEARTBREAKERS','A Action-Packed Panorama of a Technical Writer And a Man who must Build a Forensic Psychologist in A Manhattan Penthouse',2006,152,19.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (65,'TEMPLE ATTRACTION','A Action-Packed Saga of a Forensic Psychologist And a Woman who must Save a Athlete in Georgia',2007,71,13.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (66,'TENENBAUMS COMMAND','A Taut Display of a Pioneer And a Man who must Reach a Girl in The Gulf of Mexico',2008,99,24.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (67,'TEQUILA PAST','A Action-Packed Panorama of a Mad Scientist And a Robot who must Race a Student in Nigeria',2010,53,17.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (68,'TERMINATOR CLUB','A Touching Story of a Crocodile And a Girl who must Sink a Man in The Gulf of Mexico',2011,88,11.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (69,'TEXAS WATCH','A Awe-Inspiring Yarn of a Student And a Teacher who must Rescue a Teacher in An Abandoned Amusement Park',2012,179,22.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (70,'THEORY MERMAID','A Fateful Yarn of a Composer And a Monkey who must Vanquish a Athlete in The First Manned Space Station',2013,184,19.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (71,'THIEF PELICAN','A Touching Documentary of a Madman And a Mad Scientist who must Outrace a Feminist in An Abandoned Mine Shaft',2006,135,28.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (72,'THIN SAGEBRUSH','A Emotional Drama of a Husband And a Lumberjack who must Build a Cat in Ancient Greece',2007,53,19.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (73,'TIES HUNGER','A Insightful Saga of a Astronaut And a Explorer who must Find a Mad Scientist in A Submarine',2008,111,28.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (74,'TIGHT ROPE','A Thrilling story of a Boat And a Secret Agent who must Face a Boy in A Baloon',2009,172,14.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (75,'TIMBERLAND SKY','A Boring Display of a Man And a Dog who must Redeem a Girl in A Submarine',2010,69,13.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (76,'TITANIC BOONDOCK','A Brilliant Reflection of a Feminist And a Dog who must Rescue a Boy in A Baloon Factory',2011,104,18.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (77,'TITANS SOAR','A Unbelieveable Panorama of a Feminist And a Sumo Wrestler who must Race a Technical Writer in Ancient China',2012,91,11.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (78,'TOMATOES HELLRESCUERS','A Thoughtful story of a Madman And a Astronaut who must Outwit a Monkey in A Shark Tank',2013,68,23.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (79,'TOMORROW HUSTLE','A Thoughtful Story of a Moose And a Husband who must Face a Secret Agent in The Sahara Desert',2006,142,21.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (80,'TOOTSIE PILOT','A Awe-Inspiring Documentary of a Athlete And a Pastry Chef who must Defeat a Lumberjack in Berlin',2007,157,10.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (81,'TORQUE BOUND','A Emotional Display of a Crocodile And a Husband who must Reach a Man in Ancient Japan',2008,179,27.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (82,'WAIT CIDER','A Intrepid story of a Woman And a Forensic Psychologist who must Outsmart a Astronaut in A Manhattan Penthouse',2010,112,19.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (83,'WAKE JAWS','A Beautiful Saga of a Feminist And a Composer who must Race a Moose in Berlin',2011,73,18.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (84,'WALLS ARTIST','A Insightful Panorama of a Teacher And a Teacher who must Outwit a Mad Cow in An Abandoned Fun House',2012,135,19.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (85,'WANDA CHAMBER','A Insightful Drama of a A Shark And a Pioneer who must Find a Athlete in The Outback',2013,107,23.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (86,'WAR NOTTING','A Boring Drama of a Teacher And a Sumo Wrestler who must Race a Secret Agent in The Canadian Rockies',2006,80,26.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (87,'WARDROBE PHANTOM','A Action-Packed Display of a Mad Cow And a Astronaut who must Defeat a Car in Ancient India',2007,178,19.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (88,'WARLOCK WEREWOLF','A Astounding Yarn of a Pioneer And a Crocodile who must Outsmart a A Shark in The Outback',2008,83,10.99,'NR')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (89,'WARS PLUTO','A Taut Reflection of a Teacher And a Database Administrator who must Chase a Madman in The Sahara Desert',2009,128,15.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (90,'WASH BEHIND THE EARS','A Awe-Inspiring Reflection of a Cat And a Pioneer who must Escape a Hunter in Alaska',2010,161,22.99,'R')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (91,'WASTELAND DIVINE','A Fanciful Story of a Database Administrator And a Athlete who must Rescue a Database Administrator in Ancient China',2011,85,18.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (92,'WATCH TRACY','A Fast-Paced Yarn of a Dog And a Frisbee who must Help a Hunter in Ohio',2012,78,12.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (93,'WATERFRONT DELIVERANCE','A Unbelieveable Documentary of a Dentist And a Technical Writer who must Build a Athlete in Niagara Falls',2013,61,17.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (94,'WATERSHIP FRONTIER','A Emotional Yarn of a Boat And a Crocodile who must Meet a Moose in Georgia',2006,112,28.99,'G')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (95,'WEDDING APOLLO','A Action-Packed Tale of a Student And a Waitress who must Help a Lumberjack in An Abandoned Mine Shaft',2007,70,14.99,'PG')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (96,'WORLD LEATHERNECKS','A Unbelieveable Tale of a Pioneer And a Astronaut who must Outwit a Robot in An Abandoned Amusement Park',2007,171,13.99,'PG-13')''')
cursor.execute('''INSERT INTO film (filmID, title, description, releaseYear, length, replacementCost, rating) VALUES (97,'WORST BURGER EVER','A Thrilling Drama of a Madman And a Dentist who must Help a Boy in The Outback',2008,185,26.99,'PG')''')

## Display Record
print("Record: ")

data = cursor.execute('''SELECT * FROM FILM''')

for row in data:
    print(row)

## Close connection
connection.commit()
connection.close()    