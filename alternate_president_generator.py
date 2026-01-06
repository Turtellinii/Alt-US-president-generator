import random
import sys
from character_generator import generate_mbti_profile

# State admission dates (year each state joined the Union)
STATE_ADMISSION_DATES = {
    # Original 13 colonies
    "Delaware": 1787, "Pennsylvania": 1787, "New Jersey": 1787, "Georgia": 1788,
    "Connecticut": 1788, "Massachusetts": 1788, "Maryland": 1788, "South Carolina": 1788,
    "New Hampshire": 1788, "Virginia": 1788, "New York": 1788, "North Carolina": 1789,
    "Rhode Island": 1790,
    # Other states
    "Vermont": 1791, "Kentucky": 1792, "Tennessee": 1796, "Ohio": 1803,
    "Louisiana": 1812, "Indiana": 1816, "Mississippi": 1817, "Illinois": 1818,
    "Alabama": 1819, "Maine": 1820, "Missouri": 1821, "Arkansas": 1836,
    "Michigan": 1837, "Florida": 1845, "Texas": 1845, "Iowa": 1846,
    "Wisconsin": 1848, "California": 1850, "Minnesota": 1858, "Oregon": 1859,
    "Kansas": 1861, "West Virginia": 1863, "Nevada": 1864, "Nebraska": 1867,
    "Colorado": 1876, "North Dakota": 1889, "South Dakota": 1889, "Montana": 1889,
    "Washington": 1889, "Idaho": 1890, "Wyoming": 1890, "Utah": 1896,
    "Oklahoma": 1907, "New Mexico": 1912, "Arizona": 1912, "Alaska": 1959,
    "Hawaii": 1959
}

ORIGINAL_13_COLONIES = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island"
]

# Period-accurate first names by era
# Pre-2000: Traditional white American names only
# Post-2000: More diverse names reflecting modern America
FIRST_NAMES_MALE = {
    "early": ["George", "John", "Thomas", "James", "William", "Benjamin", "Samuel",
              "Joseph", "Abraham", "Daniel", "Henry", "Charles", "Robert", "Edward",
              "Andrew", "Richard", "Peter", "Jonathan", "Isaac", "Jacob", "David",
              "Nathaniel", "Elijah", "Josiah", "Ezekiel", "Solomon", "Caleb", "Seth",
              "Silas", "Ebenezer", "Jeremiah", "Timothy", "Matthias", "Zachariah",
              "Gideon", "Amos", "Rufus", "Cyrus", "Levi", "Moses", "Aaron", "Enoch",
              "Ezra", "Obadiah", "Lemuel", "Barnabas", "Cornelius", "Simeon", "Tobias",
              "Reuben", "Phinehas", "Jedediah", "Hiram", "Asher", "Ephraim", "Ichabod"],
    "mid": ["William", "James", "John", "George", "Charles", "Frank", "Henry", "Thomas",
            "Edward", "Walter", "Arthur", "Frederick", "Albert", "Harry", "Samuel",
            "Clarence", "Louis", "Theodore", "Benjamin", "Oscar", "Herbert", "Howard",
            "Eugene", "Ernest", "Ralph", "Roy", "Leon", "Earl", "Lawrence", "Alfred",
            "Chester", "Floyd", "Homer", "Lester", "Leonard", "Raymond", "Clifford",
            "Edwin", "Stanley", "Lloyd", "Calvin", "Norman", "Vernon", "Willard",
            "Elmer", "Milton", "Julius", "Harvey", "Herman", "Horace", "Virgil",
            "Francis", "Luther", "Clyde", "Russell", "Harold", "Edgar", "Percy"],
    "late": ["Robert", "James", "John", "William", "Richard", "Charles", "Donald",
             "George", "Kenneth", "Joseph", "Thomas", "David", "Edward", "Ronald",
             "Paul", "Raymond", "Harold", "Walter", "Jack", "Gerald", "Carl",
             "Dennis", "Larry", "Gary", "Roger", "Frank", "Terry", "Jerry", "Douglas",
             "Peter", "Henry", "Patrick", "Philip", "Stephen", "Gregory", "Bruce",
             "Albert", "Eugene", "Roy", "Ralph", "Arthur", "Russell", "Ernest",
             "Alan", "Lawrence", "Wayne", "Louis", "Howard", "Keith", "Randy",
             "Scott", "Timothy", "Martin", "Jeffrey", "Frederick", "Samuel", "Vincent"],
    "modern": ["Michael", "James", "Robert", "John", "David", "William", "Richard",
               "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Donald",
               "Steven", "Paul", "Mark", "George", "Kenneth", "Andrew", "Brian",
               "Joshua", "Kevin", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan",
               "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry",
               "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Raymond", "Gregory",
               "Alexander", "Patrick", "Frank", "Dennis", "Jerry", "Tyler", "Aaron",
               "Jose", "Adam", "Henry", "Nathan", "Douglas", "Zachary", "Peter", "Kyle",
               "Walter", "Ethan", "Jeremy", "Harold", "Keith", "Christian", "Roger"]
}

FIRST_NAMES_FEMALE = {
    "early": ["Martha", "Abigail", "Elizabeth", "Sarah", "Mary", "Ann", "Hannah",
              "Rebecca", "Catherine", "Margaret", "Jane", "Rachel", "Prudence",
              "Deborah", "Ruth", "Esther", "Lydia", "Phoebe", "Susannah", "Priscilla",
              "Mercy", "Charity", "Temperance", "Mehitabel", "Bathsheba", "Tabitha",
              "Naomi", "Miriam", "Judith", "Eleanor", "Charlotte", "Sophia", "Harriet",
              "Betsy", "Polly", "Sally", "Nancy", "Peggy", "Molly", "Patsy"],
    "mid": ["Mary", "Anna", "Margaret", "Helen", "Elizabeth", "Ruth", "Florence",
            "Emma", "Alice", "Grace", "Sarah", "Clara", "Lillian", "Edith", "Ethel",
            "Mabel", "Gertrude", "Bertha", "Rose", "Hazel", "Martha", "Minnie",
            "Catherine", "Nellie", "Frances", "Annie", "Bessie", "Pearl", "Myrtle",
            "Eva", "Louise", "Elsie", "Ella", "Agnes", "Josephine", "Gladys",
            "Beatrice", "Esther", "Laura", "Blanche", "Viola", "Irene", "Hilda",
            "Stella", "Ida", "Alma", "Cora", "Lena", "Ada", "Dora", "Edna"],
    "late": ["Mary", "Barbara", "Patricia", "Carol", "Sandra", "Nancy", "Sharon",
             "Judith", "Susan", "Betty", "Margaret", "Linda", "Dorothy", "Helen",
             "Karen", "Donna", "Deborah", "Cynthia", "Kathleen", "Pamela", "Brenda",
             "Virginia", "Janet", "Catherine", "Carolyn", "Ruth", "Diane", "Joyce",
             "Christine", "Frances", "Ann", "Jean", "Alice", "Janice", "Beverly",
             "Doris", "Gloria", "Evelyn", "Joan", "Cheryl", "Martha", "Judy",
             "Marilyn", "Eleanor", "Teresa", "Phyllis", "Shirley", "Bonnie", "Lois"],
    "modern": ["Jennifer", "Michelle", "Lisa", "Karen", "Angela", "Kimberly",
               "Elizabeth", "Sarah", "Jessica", "Amanda", "Melissa", "Nicole",
               "Amy", "Rebecca", "Laura", "Stephanie", "Rachel", "Catherine",
               "Emily", "Ashley", "Samantha", "Heather", "Christine", "Anna",
               "Megan", "Lauren", "Katherine", "Hannah", "Alexandra", "Danielle",
               "Brittany", "Madison", "Christina", "Olivia", "Amber", "Kelly",
               "Maria", "Susan", "Tiffany", "Michelle", "Sandra", "Kathryn",
               "Patricia", "Nancy", "Linda", "Barbara", "Margaret", "Carol",
               "Dorothy", "Betty", "Helen", "Ruth", "Sharon", "Donna", "Deborah"]
}

# Last names - traditional American surnames until 2000, more diverse after
LAST_NAMES = {
    "early": ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Hamilton",
              "Franklin", "Hancock", "Sherman", "Morris", "Wilson", "Randolph",
              "Lee", "Marshall", "Jay", "Henry", "Livingston", "Ellsworth", "Pinckney",
              "Bradford", "Winthrop", "Mather", "Brewster", "Standish", "Alden",
              "Hopkins", "Carver", "Warren", "Revere", "Knox", "Greene", "Wayne",
              "Putnam", "Stark", "Allen", "Clinton", "Burr", "Van Buren", "Calhoun"],
    "mid": ["Johnson", "Smith", "Brown", "Williams", "Jones", "Miller", "Davis",
            "Wilson", "Anderson", "Taylor", "Thomas", "Jackson", "White", "Harris",
            "Martin", "Thompson", "Robinson", "Clark", "Lewis", "Walker", "Hall",
            "Allen", "Young", "King", "Wright", "Scott", "Green", "Baker", "Adams",
            "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips",
            "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Morris",
            "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Cooper",
            "Richardson", "Cox", "Howard", "Ward", "Peterson", "Gray", "Hughes"],
    "late": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis",
             "Wilson", "Anderson", "Taylor", "Thomas", "Moore", "Jackson", "Martin",
             "Lee", "Thompson", "White", "Harris", "Clark", "Lewis", "Robinson",
             "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Green",
             "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez",
             "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards",
             "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook",
             "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson"],
    "modern": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
               "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
               "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
               "Lee", "Thompson", "White", "Harris", "Sanchez", "Clark", "Lewis",
               "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott",
               "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson",
               "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
               "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz",
               "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy"]
}

# Color names for parties
PARTY_COLORS = [
    "Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Brown", "Silver",
    "Gold", "Crimson", "Violet", "Indigo", "Scarlet", "Amber", "Emerald",
    "Sapphire", "Ruby", "Jade", "Pearl", "Ivory", "Bronze", "Copper", "Teal",
    "Magenta", "Turquoise", "Maroon", "Navy", "Olive", "Coral", "Rose"
]


def get_name_era(year):
    """Determine which era of names to use based on year"""
    if year < 1850:
        return "early"
    elif year < 1920:
        return "mid"
    elif year < 1980:
        return "late"
    else:
        return "modern"


def generate_random_name(year, is_female=False):
    """Generate a period-accurate random name"""
    era = get_name_era(year)

    if is_female:
        first_name = random.choice(FIRST_NAMES_FEMALE[era])
    else:
        first_name = random.choice(FIRST_NAMES_MALE[era])

    # Keep trying until we get a different last name
    # Prevents names like "Thomas Thomas"
    max_attempts = 100
    for _ in range(max_attempts):
        last_name = random.choice(LAST_NAMES[era])
        if first_name != last_name:
            break

    return f"{first_name} {last_name}"


def get_eligible_states(birth_year):
    """Get list of eligible states based on birth year"""
    eligible = ORIGINAL_13_COLONIES.copy()

    for state, admission_year in STATE_ADMISSION_DATES.items():
        if state not in ORIGINAL_13_COLONIES:
            # State is available if person was born 15 years or less before admission
            # or born after admission
            # Example: Indiana admitted 1816, eligible if born 1801 or later (1816 - 15 = 1801)
            if birth_year >= admission_year - 15:
                eligible.append(state)

    return eligible


def generate_wealth_score():
    """Generate wealth score based on weighted random distribution"""
    roll = random.randint(1, 54)
    if roll == 1:
        return 0
    elif 2 <= roll <= 3:
        return 1
    elif 4 <= roll <= 6:
        return 2
    elif 7 <= roll <= 10:
        return 3
    elif 11 <= roll <= 15:
        return 4
    elif 16 <= roll <= 21:
        return 5
    elif 22 <= roll <= 28:
        return 6
    elif 29 <= roll <= 36:
        return 7
    elif 37 <= roll <= 43:
        return 8
    elif 44 <= roll <= 49:
        return 9
    else:  # 50-54
        return 10


def get_wealth_class(score):
    """Convert wealth score to class description"""
    if score == 0:
        return "Homeless"
    elif 1 <= score <= 3:
        return "Lower Class"
    elif 4 <= score <= 6:
        return "Middle Class"
    elif 7 <= score <= 9:
        return "Upper Class"
    else:  # 10
        return "Elite"


def get_shift_range(score):
    """Get the shift range based on current political score

    Extreme positions have limited ability to shift further toward extremes,
    creating a natural tendency toward moderation.
    """
    if -100 <= score <= -67:
        # Far left: harder to go more left
        return (-10, 20)
    elif -66 <= score <= -34:
        # Left: somewhat harder to go more left
        return (-15, 20)
    elif -33 <= score <= 33:
        # Center: normal range
        return (-20, 20)
    elif 34 <= score <= 66:
        # Right: somewhat harder to go more right
        return (-20, 15)
    else:  # 67 to 100
        # Far right: harder to go more right
        return (-20, 10)


def check_authoritarian_tendency(president):
    """Check if president meets criteria for attempting 3+ terms

    Returns tuple: (attempts_extra_terms, reason_code)
    reason_code: 1=enneagram, 2=mbti combo, 3=president social, 4=party social
    """
    reasons_met = []

    # Condition 1: Enneagram is 8w7 or 8w9 (first XwY in personality)
    personality_parts = president.personality.split()
    if len(personality_parts) >= 3:
        enneagram = personality_parts[2]  # Third element is main enneagram
        if enneagram in ['8w7', '8w9']:
            reasons_met.append(1)

    # Condition 2: Specific MBTI + Enneagram combinations
    target_combos = [
        'ENTJ 3w4 ', 'ESTJ 3w4 ', 'ESTP 3w4 ', 'ESFP 3w4', 'INTJ 3w4', 'ENTP 3w4',
        'ENTJ 3w2', 'ESTP 3w2', 'ESFP 3w2', 'ENTP 3w2', 'ESTJ 3w2',
        'INTJ 5w6', 'ENTJ 5w6', 'ENTP 5w6',
        'ESTP 7w8', 'ESFP 7w8', 'ENTJ 7w8', 'ENTP 7w8',
        '6w7 sx/so', '6w5 sx/so', '4w3 sx/so', '4w3 sx/sp'
    ]
    for combo in target_combos:
        if combo in president.personality:
            reasons_met.append(2)
            break

    # Condition 3: President's social score >= 34
    if president.social_score >= 34:
        reasons_met.append(3)

    # Condition 4: Party's social score >= 51 (if they have a party)
    if president.party and president.party.social_score >= 51:
        reasons_met.append(4)

    # Need 2 or more conditions to attempt extra terms
    attempts = len(reasons_met) >= 2
    return attempts, reasons_met


class Party:
    """Represents a political party"""
    used_colors = set()

    def __init__(self, name, social_score, economic_score, founding_year):
        self.name = name
        self.social_score = social_score
        self.economic_score = economic_score
        self.founding_year = founding_year
        self.last_in_power = None
        self.dissolved = False

    @classmethod
    def generate_new_party(cls, year):
        """Generate a new political party with random attributes"""
        # Get available colors
        available_colors = [c for c in PARTY_COLORS if c not in cls.used_colors]
        if not available_colors:
            # If all colors used, reset and use all
            cls.used_colors.clear()
            available_colors = PARTY_COLORS.copy()

        color = random.choice(available_colors)
        cls.used_colors.add(color)

        # New parties start in moderate range (±75) with some diversity
        social_score = random.randint(-75, 75)
        economic_score = random.randint(-75, 75)

        return cls(f"{color} Party", social_score, economic_score, year)

    def shift_politics(self):
        """Randomly shift party's political positions

        Uses dynamic shift ranges based on current position to create
        natural resistance to extreme positions.
        """
        # Get shift ranges based on current positions
        social_min, social_max = get_shift_range(self.social_score)
        economic_min, economic_max = get_shift_range(self.economic_score)

        # Apply shifts with position-dependent ranges
        social_shift = random.randint(social_min, social_max)
        economic_shift = random.randint(economic_min, economic_max)

        self.social_score = max(-100, min(100, self.social_score + social_shift))
        self.economic_score = max(-100, min(100, self.economic_score + economic_shift))

    def check_dissolution(self, current_year):
        """Check if party should dissolve due to being out of power"""
        if self.last_in_power is None:
            return False

        years_out_of_power = current_year - self.last_in_power
        if years_out_of_power >= 20:
            # 1/3 chance of dissolution
            if random.randint(1, 3) == 1:
                self.dissolved = True
                return True
        return False

    def __str__(self):
        return f"{self.name} (Social: {self.social_score:+d}, Economic: {self.economic_score:+d})"


class President:
    """Represents a president"""

    def __init__(self, election_year, party=None, is_successor=False, is_first_president=False, age_range=None):
        self.election_year = election_year
        self.party = party
        self.is_successor = is_successor
        self.is_first_president = is_first_president

        # Generate gender (male until 2000, then weighted)
        if election_year < 2000:
            self.gender = "Male"
            is_female = False
        else:
            gender_roll = random.randint(1, 5)
            self.gender = "Female" if gender_roll == 5 else "Male"
            is_female = (gender_roll == 5)

        # Generate name
        self.name = generate_random_name(election_year, is_female)

        # Generate personality using character generator
        # Pass 'M' or 'F' to match the president's gender
        gender_code = 'F' if is_female else 'M'
        self.personality = generate_mbti_profile(gender_code)

        # Generate physical appearance
        # Hair color: 51% brown, 28% blonde, 12% black, 9% red
        hair_roll = random.randint(1, 100)
        if hair_roll <= 51:
            self.hair_color = "Brown"
        elif hair_roll <= 79:
            self.hair_color = "Blonde"
        elif hair_roll <= 91:
            self.hair_color = "Black"
        else:
            self.hair_color = "Red"

        # Hair texture: 25% straight, 50% wavy, 25% curly
        texture_roll = random.randint(1, 100)
        if texture_roll <= 25:
            self.hair_texture = "Straight"
        elif texture_roll <= 75:
            self.hair_texture = "Wavy"
        else:
            self.hair_texture = "Curly"

        # Eye color: 46% brown, 27% blue, 18% hazel, 9% green
        eye_roll = random.randint(1, 100)
        if eye_roll <= 46:
            self.eye_color = "Brown"
        elif eye_roll <= 73:
            self.eye_color = "Blue"
        elif eye_roll <= 91:
            self.eye_color = "Hazel"
        else:
            self.eye_color = "Green"

        # Height: 5'4" to 6'4" for males, 4'11" to 5'11" for females
        if is_female:
            height_inches = random.randint(59, 71)  # 4'11" to 5'11"
        else:
            height_inches = random.randint(64, 76)  # 5'4" to 6'4"
        feet = height_inches // 12
        inches = height_inches % 12
        self.height = f"{feet}'{inches}\""

        # Build: 30% thin, 20% muscular, 40% average, 10% fat
        build_roll = random.randint(1, 100)
        if build_roll <= 30:
            self.build = "Thin"
        elif build_roll <= 50:
            self.build = "Muscular"
        elif build_roll <= 90:
            self.build = "Average"
        else:
            self.build = "Fat"

        # Determine if dies during presidency
        death_roll = random.randint(1, 45)
        if death_roll <= 37:
            self.dies_in_office = False
            self.death_cause = None
        elif 38 <= death_roll <= 41:
            self.dies_in_office = True
            self.death_cause = "Natural Causes"
        else:  # 42-45
            self.dies_in_office = True
            self.death_cause = "Assassination"

        # Determine number of terms
        term_roll = random.randint(1, 46)
        if term_roll <= 16:
            self.num_terms = 1
        else:
            self.num_terms = 2

        # Calculate term years
        # First president (1789) starts immediately, others start year after election
        if is_first_president:
            self.term_start = election_year  # 1789
            self.term_end = election_year + (self.num_terms * 4) - 1  # 1792 or 1796
        else:
            self.term_start = election_year + 1
            self.term_end = election_year + (self.num_terms * 4)

        self.completed_term_end = self.term_end

        # If dies in office, determine when
        self.death_year = None
        if self.dies_in_office:
            # If they serve 2 terms, they can only die in the second term
            # (because if they died in the first term, they wouldn't be reelected)
            if self.num_terms == 2:
                # Die in second term only (years 5-8 of presidency)
                second_term_start = self.term_start + 4
                self.death_year = random.randint(second_term_start, self.term_end)
            else:
                # Single term - can die anytime during the term
                self.death_year = random.randint(self.term_start, self.term_end)
            self.term_end = self.death_year

        # Generate political compass scores
        if party is None:
            # First president, no party
            self.social_score = random.randint(-100, 100)
            self.economic_score = random.randint(-100, 100)
        else:
            # Add individual variation to party scores
            # Wider variance allows for more diversity in authoritarian tendencies
            # Clamp to -100 to 100 range
            personal_social = random.randint(-40, 40)
            personal_economic = random.randint(-40, 40)
            self.social_score = max(-100, min(100, party.social_score + personal_social))
            self.economic_score = max(-100, min(100, party.economic_score + personal_economic))

        # Generate life years
        # Birth year: election year - random age
        # Use custom age range if provided (for dictator successors), otherwise default 35-70
        if age_range:
            age_at_election = random.randint(age_range[0], age_range[1])
        else:
            age_at_election = random.randint(35, 70)
        self.birth_year = election_year - age_at_election

        # Death year based on era (lowered minimum lifespans)
        if election_year < 1800:
            lifespan = random.randint(55, 80)
            lifespan_range = "55-80 (< 1800)"
        elif election_year < 1851:
            lifespan = random.randint(55, 85)
            lifespan_range = "55-85 (< 1851)"
        elif election_year < 1900:
            lifespan = random.randint(60, 90)
            lifespan_range = "60-90 (< 1900)"
        elif election_year < 1951:
            lifespan = random.randint(60, 95)
            lifespan_range = "60-95 (< 1951)"
        elif election_year < 2001:
            lifespan = random.randint(65, 100)
            lifespan_range = "65-100 (< 2001)"
        else:
            lifespan = random.randint(65, 105)
            lifespan_range = "65-105 (>= 2001)"

        # Store lifespan as attribute for dictator successors
        self.lifespan = lifespan
        natural_death_year = self.birth_year + lifespan

        # Debug logging for dictator successors
        if party is None and not is_first_president:
            print(f"[DEBUG SUCCESSOR] election_year={election_year}, birth_year={self.birth_year}, lifespan={lifespan} (range: {lifespan_range}), natural_death={natural_death_year}")

        # If died in office, use that death year, otherwise use natural
        # But ensure they live at least until after their presidency
        if self.dies_in_office:
            self.final_death_year = self.death_year
        else:
            # They must live at least one year after their term ends
            min_death_year = self.completed_term_end + 1
            self.final_death_year = max(natural_death_year, min_death_year)

        # Generate state of origin
        self.state = random.choice(get_eligible_states(self.birth_year))

        # Generate wealth score
        self.wealth_score = generate_wealth_score()
        self.wealth_class = get_wealth_class(self.wealth_score)

        self.successor = None

    def __str__(self):
        party_str = self.party.name if self.party else "No Party"
        terms_str = f"{self.num_terms} term{'s' if self.num_terms > 1 else ''}"

        result = [
            f"\n{'='*80}",
            f"President: {self.name} ({self.gender})",
            f"Election Year: {self.election_year}",
            f"Term: {self.term_start}-{self.term_end}",
            f"Party: {party_str}",
            f"Number of Terms: {terms_str}",
        ]

        if self.dies_in_office:
            result.append(f"Death in Office: {self.death_year} ({self.death_cause})")

        result.extend([
            f"Political Position: Social {self.social_score:+d}, Economic {self.economic_score:+d}",
            f"Life: {self.birth_year}-{self.final_death_year} ({self.final_death_year - self.birth_year} years)",
            f"State of Origin: {self.state}",
            f"Wealth: {self.wealth_class} (Score: {self.wealth_score}/10)",
            f"Personality: {self.personality}",
            f"Appearance: {self.hair_texture} {self.hair_color} hair, {self.eye_color} eyes, {self.height}, {self.build} build",
        ])

        if self.successor:
            result.append(f"\nSuccessor (due to death in office):")
            result.append(str(self.successor))

        result.append('='*80)

        return '\n'.join(result)


class AlternateHistoryGenerator:
    """Main generator for alternate US history"""

    def __init__(self):
        self.parties = []
        self.presidents = []
        self.current_year = 1789

        # Authoritarian regime tracking
        self.is_authoritarian = False
        self.regime_type = None  # 'one_party', 'dictatorship', or 'hybrid'
        self.regime_party = None  # The ruling party (if applicable)
        self.current_dictator = None  # Current dictator (if applicable)
        self.revolution_attempt_chance = 10  # Starts at 10%
        self.revolution_success_chance = 10  # Starts at 10%
        self.regime_start_year = None  # Year the regime was established
        self.last_revolution_check_year = None  # Last year a revolution check was performed
        self.scheduled_election_year = None  # For one-party states: when the next election is scheduled

    def initialize_parties(self):
        """Initialize political parties in 1792"""
        num_parties = random.randint(2, 4)
        print(f"\n{num_parties} political parties formed in 1792:\n")

        for _ in range(num_parties):
            party = Party.generate_new_party(1792)
            self.parties.append(party)
            print(f"  {party}")

    def check_new_party_formation(self, year):
        """Check if a new party should form this election"""
        active_parties = [p for p in self.parties if not p.dissolved]
        num_active = len(active_parties)

        if num_active == 0:
            return  # Safety check

        # 1/x chance where x is number of current parties
        if random.randint(1, num_active) == 1:
            new_party = Party.generate_new_party(year)
            self.parties.append(new_party)
            print(f"\nNew party formed: {new_party}")

    def shift_party_politics(self):
        """Shift all active parties' political positions"""
        for party in self.parties:
            if not party.dissolved:
                party.shift_politics()

    def check_party_dissolutions(self, year):
        """Check if any parties should dissolve"""
        for party in self.parties:
            if not party.dissolved and party.check_dissolution(year):
                print(f"\n{party.name} has dissolved after {year - party.last_in_power} years out of power.")

    def check_party_mergers(self, year):
        """Check if any parties should merge due to political similarity"""
        active_parties = [p for p in self.parties if not p.dissolved]

        # Check all pairs of parties
        for i in range(len(active_parties)):
            for j in range(i + 1, len(active_parties)):
                party1 = active_parties[i]
                party2 = active_parties[j]

                # Check if within 20 points on both axes
                social_diff = abs(party1.social_score - party2.social_score)
                economic_diff = abs(party1.economic_score - party2.economic_score)

                if social_diff <= 20 and economic_diff <= 20:
                    # Parties should merge
                    # Extract color names (remove " Party" suffix)
                    color1 = party1.name.replace(" Party", "")
                    color2 = party2.name.replace(" Party", "")
                    merged_name = f"{color1}-{color2} Party"

                    # Calculate average scores
                    merged_social = (party1.social_score + party2.social_score) // 2
                    merged_economic = (party1.economic_score + party2.economic_score) // 2

                    # Create merged party
                    merged_party = Party(merged_name, merged_social, merged_economic, year)

                    # Take the most recent last_in_power
                    if party1.last_in_power is not None and party2.last_in_power is not None:
                        merged_party.last_in_power = max(party1.last_in_power, party2.last_in_power)
                    elif party1.last_in_power is not None:
                        merged_party.last_in_power = party1.last_in_power
                    elif party2.last_in_power is not None:
                        merged_party.last_in_power = party2.last_in_power

                    print(f"\n🤝 {party1.name} and {party2.name} have MERGED into {merged_name}")
                    print(f"   New position: Social {merged_social:+d}, Economic {merged_economic:+d}")

                    # Dissolve old parties
                    party1.dissolved = True
                    party2.dissolved = True

                    # Add merged party
                    self.parties.append(merged_party)

                    # Only merge one pair per cycle to avoid complex cascading
                    return

    def generate_president(self, year, party=None, is_successor=False, is_first_president=False):
        """Generate a new president"""
        president = President(year, party, is_successor, is_first_president)

        # Update party's last_in_power to when they leave office (term end)
        if party:
            party.last_in_power = president.completed_term_end

        return president

    def generate_successor(self, deceased_president):
        """Generate a successor when a president dies in office"""
        # Successor from same party, continues the term
        # The "election_year" for successor is the year of the next actual election (original term end)
        original_term_end = deceased_president.completed_term_end
        successor = President(original_term_end, deceased_president.party, is_successor=True)

        # Override the automatic term calculation since this is a succession
        # Successor takes office immediately upon death
        successor.term_start = deceased_president.death_year
        successor.term_end = original_term_end

        # Check if successor gets reelected for additional terms
        reelection_roll = random.randint(1, 2)
        if reelection_roll == 2:
            # Reelected - determine number of additional terms
            term_roll = random.randint(1, 46)
            if term_roll <= 16:
                additional_terms = 1
            else:
                additional_terms = 2

            # Update election year and term end for the reelection
            successor.election_year = original_term_end
            successor.num_terms = additional_terms
            successor.term_end = original_term_end + (additional_terms * 4)
        else:
            # Not reelected - only completes original term
            successor.election_year = deceased_president.election_year  # They weren't elected themselves
            successor.num_terms = 0  # Didn't serve a full elected term
            successor.term_end = original_term_end

        # Fix death_year if dies_in_office is True
        # The death_year was calculated in __init__ using the wrong term_start/term_end
        # Recalculate it using the corrected values
        if successor.dies_in_office:
            if successor.num_terms >= 2:
                # Die in second term only (4 years after term_start)
                second_term_start = successor.term_start + 4
                successor.death_year = random.randint(second_term_start, successor.term_end)
            else:
                # Single term or partial term - can die anytime during the term
                successor.death_year = random.randint(successor.term_start, successor.term_end)
            successor.term_end = successor.death_year

        return successor

    def attempt_term_extension(self, president, current_year):
        """Handle president attempting 3rd and 4th terms

        Returns tuple: (got_third_term, got_fourth_term, authoritarian_type)
        """
        # CRITICAL: Check if president will die before completing a 3rd term
        # We must check final_death_year, not just dies_in_office
        third_term_end = president.term_end + 4

        # If president died during their first 2 terms, they can't attempt extensions
        if president.dies_in_office:
            return False, False, None

        # If president will die before the 3rd term ends, they can't attempt it
        if president.final_death_year < third_term_end:
            return False, False, None

        attempts, reasons = check_authoritarian_tendency(president)

        if not attempts:
            return False, False, None

        # Store original 2-term end date before any modifications
        original_two_term_end = president.term_end
        
        print(f"\n⚠️  {president.name} attempts to run for a THIRD TERM!")
        print(f"   Reasons: {', '.join(['Enneagram 8w7/8w9' if 1 in reasons else '', 'MBTI combo' if 2 in reasons else '', 'High personal auth score' if 3 in reasons else '', 'High party auth score' if 4 in reasons else ''])}")

        # 50% chance of getting 3rd term
        if random.randint(1, 100) <= 50:
            print(f"   ✓ Third term GRANTED! ({president.term_end+1}-{president.term_end+4})")
            president.num_terms = 3
            president.term_end += 4
            president.completed_term_end = president.term_end
            
            # Check if they will die during 3rd term based on final_death_year
            third_term_start = original_two_term_end + 1
            if president.final_death_year <= president.term_end:
                # They will die during the 3rd term
                president.dies_in_office = True
                president.death_year = president.final_death_year
                president.death_cause = "Natural Causes" if random.randint(1, 2) == 1 else "Assassination"
                president.term_end = president.death_year
                print(f"\n💀 {president.name} dies during their third term in {president.death_year}")
                return True, False, None
        else:
            print(f"   ✗ Third term DENIED by voters")
            return False, False, None
        
        # Now attempt 4th term (40% chance)
        print(f"\n⚠️  {president.name} attempts to run for a FOURTH TERM!")
        if random.randint(1, 100) <= 40:
            print(f"   ✓ Fourth term GRANTED! ({president.term_end+1}-{president.term_end+4})")
            president.num_terms = 4
            president.term_end += 4
            president.completed_term_end = president.term_end

            # Check if they will die during the 4th term
            fourth_term_start = president.term_end - 4 + 1
            if president.final_death_year < president.term_end:
                # They will die during the 4th term, before completing it
                president.dies_in_office = True
                president.death_year = president.final_death_year
                president.death_cause = "Natural Causes" if random.randint(1, 2) == 1 else "Assassination"
                president.term_end = president.death_year
                print(f"\n💀 {president.name} dies during their fourth term in {president.death_year}")
                print(f"   No authoritarian takeover possible")
                return True, False, None

            # Determine authoritarian type based on which conditions are met
            # Priority system for more balanced regime distribution
            if 1 in reasons:
                # Condition 1 (8w7/8w9 personality) takes precedence
                if 3 in reasons:
                    # 1 + 3 (with or without 4) = Dictatorship
                    # Strong personality + high personal score = personal power grab
                    auth_type = 'dictatorship'
                elif 4 in reasons:
                    # 1 + 4 (without 3) = Hybrid
                    # Strong personality + party support = hybrid regime
                    auth_type = 'hybrid'
                else:
                    # Shouldn't happen (need 2+ conditions), but default
                    auth_type = 'dictatorship'
            elif 2 in reasons:
                # Condition 2 (MBTI combo)
                if 3 in reasons and 4 in reasons:
                    # 2 + 3 + 4 = Compare scores
                    # MBTI combo + both scores: stronger score determines type
                    if president.social_score > president.party.social_score:
                        auth_type = 'dictatorship'
                    else:
                        auth_type = 'hybrid'
                elif 3 in reasons:
                    # 2 + 3 (without 4) = Dictatorship
                    # MBTI combo + personal score = personal authoritarianism
                    auth_type = 'dictatorship'
                elif 4 in reasons:
                    # 2 + 4 (without 3) = One-party
                    # MBTI combo + party score = party-driven authoritarianism
                    auth_type = 'one_party'
                else:
                    # Shouldn't happen
                    auth_type = 'dictatorship'
            else:
                # Only conditions 3 and/or 4 (no personality conditions)
                if 3 in reasons and 4 in reasons:
                    # Both scores, no personality - compare strengths
                    if president.social_score > president.party.social_score:
                        auth_type = 'dictatorship'
                    else:
                        auth_type = 'hybrid'
                elif 3 in reasons:
                    # Only personal score
                    auth_type = 'dictatorship'
                elif 4 in reasons:
                    # Only party score
                    auth_type = 'one_party'
                else:
                    # Shouldn't happen (need 2+ conditions)
                    auth_type = 'dictatorship'

            return True, True, auth_type
        else:
            print(f"   ✗ Fourth term DENIED by voters")
            return True, False, None

    def attempt_authoritarian_takeover(self, president, auth_type):
        """Attempt authoritarian takeover after 4th term

        Returns True if successful, False if failed
        """
        print(f"\n🚨 {president.name} attempts AUTHORITARIAN TAKEOVER!")
        print(f"   Type: {auth_type.upper().replace('_', ' ')}")

        # 60% chance of success
        if random.randint(1, 100) <= 60:
            print(f"   ✓ TAKEOVER SUCCESSFUL!")
            self.is_authoritarian = True
            self.regime_type = auth_type
            # Regime starts in the year of the takeover (end of 4th term)
            self.regime_start_year = president.term_end
            self.last_revolution_check_year = None

            # For dictatorships and hybrid regimes, check if dictator is assassinated
            if auth_type in ['dictatorship', 'hybrid']:
                assassination_roll = random.randint(1, 45)
                print(f"[DEBUG] Assassination roll for {president.name}: {assassination_roll}/45 (assassinated if <= 8)")
                if assassination_roll <= 8:
                    # Will be assassinated
                    natural_death_year = president.final_death_year
                    # Assassination happens sometime between takeover and natural death
                    president.final_death_year = random.randint(president.term_end + 1, natural_death_year)
                    president.death_cause = "Assassination"
                    print(f"   ⚠️  {president.name} will be ASSASSINATED in {president.final_death_year}")

            if auth_type == 'one_party':
                # One-party state: eliminate all other parties
                self.regime_party = president.party
                print(f"\n🏛️  ONE-PARTY STATE ESTABLISHED")
                print(f"   Ruling party: {president.party.name}")
                print(f"   All other parties have been ELIMINATED")

                for party in self.parties:
                    if party != president.party:
                        party.dissolved = True

            elif auth_type == 'dictatorship':
                # Dictatorship: eliminate all parties
                print(f"\n👑 DICTATORSHIP ESTABLISHED")
                print(f"   Dictator: {president.name}")
                print(f"   All political parties have been ELIMINATED")

                for party in self.parties:
                    party.dissolved = True

                self.current_dictator = president

            elif auth_type == 'hybrid':
                # Hybrid: eliminate all but ruling party
                self.regime_party = president.party
                self.current_dictator = president
                print(f"\n⚡ HYBRID REGIME ESTABLISHED (Dictatorship + One-Party State)")
                print(f"   Dictator: {president.name}")
                print(f"   Ruling party: {president.party.name}")
                print(f"   All other parties have been ELIMINATED")

                for party in self.parties:
                    if party != president.party:
                        party.dissolved = True

            return True
        else:
            print(f"   ✗ TAKEOVER FAILED!")
            print(f"   {president.name} has been IMPRISONED")

            # Only eliminate party if they were complicit in the regime attempt
            # Dictatorships are personal power grabs - party not necessarily involved
            # One-party and hybrid regimes require party involvement
            if auth_type in ['one_party', 'hybrid']:
                print(f"   {president.party.name} has been ELIMINATED")
                president.party.dissolved = True
            else:
                # Dictatorship attempt - party survives and disavows the president
                print(f"   {president.party.name} disavows {president.name}")

            return False

    def generate_family_successor(self, dictator):
        """Generate a family member to succeed a dictator

        Generates a full president with all normal details, but overrides:
        - Last name (same as dictator)
        - State of origin (same as dictator)
        - Party (None - dictators have no party)
        - Wealth (equal to or greater than dictator)
        - Political scores (based on predecessor with variance)
        - Assassination chance (8/45)
        """
        succession_year = dictator.death_year if dictator.dies_in_office else dictator.final_death_year

        # Calculate age range for successor (at least 15 years younger, as young as 15)
        dictator_age_at_death = dictator.final_death_year - dictator.birth_year
        max_successor_age = dictator_age_at_death - 15
        min_successor_age = 15

        # Ensure valid range
        if max_successor_age < min_successor_age:
            max_successor_age = min_successor_age

        # Create successor with custom age range
        successor = President(succession_year, party=None, age_range=(min_successor_age, max_successor_age))

        # Override name to keep family last name
        last_name = dictator.name.split()[1]
        first_name = successor.name.split()[0]  # Keep the randomly generated first name
        successor.name = f"{first_name} {last_name}"

        # Override state to match dictator
        successor.state = dictator.state

        # Override wealth to be equal to or greater than predecessor
        # If dictator had wealth X, successor gets X to 10
        min_wealth = dictator.wealth_score
        successor.wealth_score = random.randint(min_wealth, 10)
        successor.wealth_class = get_wealth_class(successor.wealth_score)

        # Generate political scores based on predecessor with variance
        political_variance_social = random.randint(-50, 50)
        political_variance_economic = random.randint(-50, 50)
        successor.social_score = max(-100, min(100, dictator.social_score + political_variance_social))
        successor.economic_score = max(-100, min(100, dictator.economic_score + political_variance_economic))

        # Inherit some physical appearance from predecessor (family resemblance)
        # Hair color: 50% chance to inherit
        if random.randint(1, 2) == 1:
            successor.hair_color = dictator.hair_color
        # else keep the randomly generated one

        # Hair texture: 50% chance to inherit
        if random.randint(1, 2) == 1:
            successor.hair_texture = dictator.hair_texture

        # Eye color: 50% chance to inherit
        if random.randint(1, 2) == 1:
            successor.eye_color = dictator.eye_color

        # Build: 50% chance to inherit
        if random.randint(1, 2) == 1:
            successor.build = dictator.build

        # Height: Within ±5 inches of predecessor
        # Parse predecessor's height
        dictator_height_parts = dictator.height.replace('"', '').split("'")
        dictator_feet = int(dictator_height_parts[0])
        dictator_inches = int(dictator_height_parts[1])
        dictator_total_inches = dictator_feet * 12 + dictator_inches

        # Generate height within ±5 inches (with gender-specific bounds)
        if successor.gender == "Female":
            absolute_min = 59  # 4'11"
            absolute_max = 71  # 5'11"
        else:
            absolute_min = 64  # 5'4"
            absolute_max = 76  # 6'4"

        min_height = max(absolute_min, dictator_total_inches - 5)
        max_height = min(absolute_max, dictator_total_inches + 5)
        successor_height_inches = random.randint(min_height, max_height)
        successor_feet = successor_height_inches // 12
        successor_inches = successor_height_inches % 12
        successor.height = f"{successor_feet}'{successor_inches}\""

        # Set term details for dictator
        successor.term_start = succession_year + 1
        successor.term_end = succession_year + 50  # Placeholder, will rule until death
        successor.completed_term_end = successor.term_end
        successor.num_terms = 999  # Special marker for dictator

        # Fix final_death_year to use natural death (not dies_in_office)
        # President.__init__ may have set wrong final_death_year if they rolled dies_in_office
        # Use the original lifespan that was calculated
        natural_death_year = successor.birth_year + successor.lifespan
        successor.final_death_year = natural_death_year

        # Determine if assassinated (8/45 chance)
        assassination_roll = random.randint(1, 45)
        print(f"[DEBUG] Assassination roll for {successor.name}: {assassination_roll}/45 (assassinated if <= 8)")
        if assassination_roll <= 8:
            # Will be assassinated
            # Assassination happens sometime between assuming power and natural death
            successor.final_death_year = random.randint(successor.term_start, natural_death_year)
            successor.death_cause = "Assassination"

            print(f"\n👑 New Dictator: {successor.name} (family member)")
            print(f"   Assumed Power: {successor.term_start}")
            print(f"   Born: {successor.birth_year}")
            print(f"   From: {successor.state}")
            print(f"   Gender: {successor.gender}")
            print(f"   Political Position: Social {successor.social_score:+d}, Economic {successor.economic_score:+d}")
            print(f"   Wealth: {successor.wealth_class} (Score: {successor.wealth_score}/10)")
            print(f"   Life: {successor.birth_year}-{successor.final_death_year} ({successor.final_death_year - successor.birth_year} years) - ASSASSINATED")
            print(f"   Personality: {successor.personality}")
            print(f"   Appearance: {successor.hair_texture} {successor.hair_color} hair, {successor.eye_color} eyes, {successor.height}, {successor.build} build")
        else:
            # Dies naturally
            successor.death_cause = None

            print(f"\n👑 New Dictator: {successor.name} (family member)")
            print(f"   Assumed Power: {successor.term_start}")
            print(f"   Born: {successor.birth_year}")
            print(f"   From: {successor.state}")
            print(f"   Gender: {successor.gender}")
            print(f"   Political Position: Social {successor.social_score:+d}, Economic {successor.economic_score:+d}")
            print(f"   Wealth: {successor.wealth_class} (Score: {successor.wealth_score}/10)")
            print(f"   Life: {successor.birth_year}-{successor.final_death_year} ({successor.final_death_year - successor.birth_year} years)")
            print(f"   Personality: {successor.personality}")
            print(f"   Appearance: {successor.hair_texture} {successor.hair_color} hair, {successor.eye_color} eyes, {successor.height}, {successor.build} build")

        # Dictator rules until natural death or assassination - no predetermined death in office
        successor.dies_in_office = False
        successor.death_year = None

        return successor

    def check_democracy_restoration(self, year):
        """Check if authoritarian leader voluntarily restores democracy"""
        # Get current leader's social score and personality
        leader_social_score = None
        leader_name = None
        leader_personality = None

        if self.regime_type in ['dictatorship', 'hybrid'] and self.current_dictator:
            leader_social_score = self.current_dictator.social_score
            leader_name = self.current_dictator.name
            leader_personality = self.current_dictator.personality
        elif self.regime_type == 'one_party':
            # Find the current president in one-party state
            # This would be the most recent president
            if self.presidents:
                current_president = self.presidents[-1]
                leader_social_score = current_president.social_score
                leader_name = current_president.name
                leader_personality = current_president.personality

        # Check if leader has 8w7 or 8w9 enneagram (too power-hungry to restore democracy)
        if leader_personality and ('8w7' in leader_personality or '8w9' in leader_personality):
            return False  # 8w7 and 8w9 types never voluntarily give up power

        # Only check if leader has negative social score
        if leader_social_score is not None and leader_social_score < 0:
            restoration_chance = abs(leader_social_score) // 2

            print(f"\n🕊️  Democracy restoration check (Year {year})...")
            print(f"   Leader: {leader_name} (Social Score: {leader_social_score:+d})")
            print(f"   Restoration chance: {restoration_chance}%")

            if random.randint(1, 100) <= restoration_chance:
                print(f"   ✓ {leader_name} has voluntarily RESTORED DEMOCRACY!")
                print(f"   🎉 DEMOCRACY RESTORED!")

                # Reset regime (peaceful transition - no imprisonments)
                self.is_authoritarian = False
                self.regime_type = None
                self.regime_party = None
                self.current_dictator = None
                self.revolution_attempt_chance = 10
                self.revolution_success_chance = 10
                self.regime_start_year = None
                self.last_revolution_check_year = None

                # Form new parties
                num_parties = random.randint(2, 4)
                print(f"\n   {num_parties} new political parties formed:")
                for _ in range(num_parties):
                    new_party = Party.generate_new_party(year)
                    self.parties.append(new_party)
                    print(f"     {new_party}")

                return True  # Democracy restored
            else:
                print(f"   ✗ Democracy not restored")

        return False  # No restoration

    def check_revolution(self, year):
        """Check for revolution attempt and potential success"""
        # Debug output
        if self.regime_start_year is not None:
            years_elapsed = year - self.regime_start_year
            print(f"[DEBUG] Revolution check called: year={year}, regime_start={self.regime_start_year}, elapsed={years_elapsed}")

        # Only check every 4 years starting 4 years after takeover
        years_elapsed = year - self.regime_start_year

        # Check if it's time for a revolution check (every 4 years)
        if years_elapsed > 0 and years_elapsed % 4 == 0:
            # Only check if we haven't already checked this year
            if year != self.last_revolution_check_year:
                self.last_revolution_check_year = year

                # First check for top-down democracy restoration
                if self.check_democracy_restoration(year):
                    return True  # Democracy restored peacefully

                print(f"\n🎲 Revolution check (Year {year})...")
                print(f"   Attempt chance: {self.revolution_attempt_chance}%")

                # Check if revolution is attempted
                if random.randint(1, 100) <= self.revolution_attempt_chance:
                    print(f"   ⚔️  REVOLUTION ATTEMPTED!")
                    print(f"   Success chance: {self.revolution_success_chance}%")

                    # Check if revolution succeeds
                    if random.randint(1, 100) <= self.revolution_success_chance:
                        print(f"   ✓ REVOLUTION SUCCESSFUL!")
                        print(f"   🎉 DEMOCRACY RESTORED!")

                        # Imprison current leader
                        if self.current_dictator:
                            print(f"   {self.current_dictator.name} has been IMPRISONED")

                        # Eliminate ruling party if it exists
                        if self.regime_party:
                            print(f"   {self.regime_party.name} has been ELIMINATED")
                            self.regime_party.dissolved = True

                        # Reset regime
                        self.is_authoritarian = False
                        self.regime_type = None
                        self.regime_party = None
                        self.current_dictator = None
                        self.revolution_attempt_chance = 10
                        self.revolution_success_chance = 10
                        self.regime_start_year = None
                        self.last_revolution_check_year = None

                        # Form new parties
                        num_parties = random.randint(2, 4)
                        print(f"\n   {num_parties} new political parties formed:")
                        for _ in range(num_parties):
                            new_party = Party.generate_new_party(year)
                            self.parties.append(new_party)
                            print(f"     {new_party}")

                        return True  # Revolution succeeded
                    else:
                        print(f"   ✗ Revolution FAILED")
                        # Increase success chance for next attempt
                        self.revolution_success_chance = min(100, self.revolution_success_chance + 20)
                        print(f"   Next revolution success chance: {self.revolution_success_chance}%")
                else:
                    print(f"   No revolution attempted this cycle")

                # Increase attempt chance for next cycle
                self.revolution_attempt_chance = min(100, self.revolution_attempt_chance + 10)

        return False  # No revolution or failed revolution

    def run_simulation(self):
        """Run the full alternate history simulation from 1789 to 2024"""
        print("="*80)
        print("ALTERNATE US PRESIDENTIAL HISTORY GENERATOR")
        print("="*80)

        # First president (1789, no party, starts immediately)
        print(f"\nGenerating first president (1789)...")
        first_president = self.generate_president(1789, party=None, is_first_president=True)
        self.presidents.append(first_president)
        print(first_president)

        # Check for term extension attempt
        got_third, got_fourth, auth_type = self.attempt_term_extension(first_president, first_president.term_end)

        # Next election happens in the year the term ends
        next_election_year = first_president.completed_term_end
        if first_president.dies_in_office:
            successor = self.generate_successor(first_president)
            first_president.successor = successor
            self.presidents.append(successor)
            next_election_year = successor.term_end
            print(f"\nSuccessor for {first_president.name}:")
            print(successor)

            # Check if successor should attempt term extensions (if they got 2 full elected terms)
            if successor.num_terms == 2:
                got_third_succ, got_fourth_succ, auth_type_succ = self.attempt_term_extension(successor, successor.term_end)
                if got_fourth_succ and auth_type_succ:
                    if not self.attempt_authoritarian_takeover(successor, auth_type_succ):
                        # Takeover failed
                        pass
                # Update next election year if successor got extensions
                next_election_year = successor.term_end

        # Handle authoritarian takeover if president got 4th term
        if got_fourth and auth_type:
            if not self.attempt_authoritarian_takeover(first_president, auth_type):
                # Takeover failed, hold special election
                print(f"\n🗳️  SPECIAL ELECTION held in {next_election_year}")

        # Initialize parties in 1792 (only if not under authoritarian regime)
        if not self.is_authoritarian:
            self.initialize_parties()

        # Continue elections until 2024
        while next_election_year <= 2024:
            year = next_election_year
            revolution_succeeded = False

            # Check for revolution if under authoritarian regime
            if self.is_authoritarian:
                revolution_succeeded = self.check_revolution(year)
                
                if revolution_succeeded:
                    # Revolution succeeded, hold special election
                    print(f"\n🗳️  SPECIAL ELECTION in {year}")
                    self.scheduled_election_year = None
                elif self.regime_type in ['dictatorship', 'hybrid']:
                    # Under dictatorship/hybrid, check if dictator dies
                    if self.current_dictator and year >= self.current_dictator.final_death_year:
                        if self.current_dictator.death_cause == "Assassination":
                            print(f"\n💀 Dictator {self.current_dictator.name} has been ASSASSINATED")
                            print(f"   Life: {self.current_dictator.birth_year}-{self.current_dictator.final_death_year} ({self.current_dictator.final_death_year - self.current_dictator.birth_year} years)")
                        else:
                            print(f"\n💀 Dictator {self.current_dictator.name} has died")
                            print(f"   Life: {self.current_dictator.birth_year}-{self.current_dictator.final_death_year} ({self.current_dictator.final_death_year - self.current_dictator.birth_year} years)")

                        if self.regime_type == 'dictatorship':
                            # Pure dictatorship: family succession
                            self.current_dictator = self.generate_family_successor(self.current_dictator)
                            self.presidents.append(self.current_dictator)

                            # Calculate next revolution check year (aligned to regime_start_year)
                            years_since_regime = year - self.regime_start_year
                            years_to_next_check = 4 - (years_since_regime % 4) if years_since_regime % 4 != 0 else 4
                            next_election_year = year + years_to_next_check
                            continue
                        else:
                            # Hybrid: dictator's death triggers transition to one-party elections
                            # The dictator was ruling indefinitely, so we need to figure out what term they were in
                            # For simplicity, treat it as if they were in a 4-year term that would end 
                            # at the next 4-year mark from regime start
                            
                            print(f"   Generating successor to complete term...")
                            
                            # Calculate what the current "term" would have been
                            # Find the next 4-year interval from regime start
                            years_since_regime = self.current_dictator.final_death_year - self.regime_start_year
                            remaining_years_in_term = 4 - (years_since_regime % 4)
                            if remaining_years_in_term == 4:
                                remaining_years_in_term = 0  # Just started a new term
                            term_end = self.current_dictator.final_death_year + remaining_years_in_term
                            
                            # Generate a successor as a regular president
                            successor = President(term_end, self.regime_party)
                            
                            # Override term details - they're completing the dictator's term
                            successor.term_start = self.current_dictator.final_death_year
                            successor.term_end = term_end
                            successor.completed_term_end = term_end
                            successor.election_year = term_end  # Will be "elected" when term ends
                            
                            # Determine how many terms they'll serve AFTER completing this partial term
                            # Roll for 1 or 2 terms
                            term_roll = random.randint(1, 46)
                            if term_roll <= 16:
                                successor.num_terms = 1
                            else:
                                successor.num_terms = 2
                            
                            # Add their own terms after completing the partial term
                            successor.term_end = term_end + (successor.num_terms * 4)
                            successor.completed_term_end = successor.term_end

                            # Fix death_year if dies_in_office is True
                            # The death_year was calculated in __init__ using the wrong term_start/term_end
                            # Recalculate it using the corrected values
                            if successor.dies_in_office:
                                if successor.num_terms >= 2:
                                    # Die in second term only (4 years after term_start)
                                    second_term_start = successor.term_start + 4
                                    successor.death_year = random.randint(second_term_start, successor.term_end)
                                else:
                                    # Single term or partial term - can die anytime during the term
                                    successor.death_year = random.randint(successor.term_start, successor.term_end)
                                successor.term_end = successor.death_year

                            self.presidents.append(successor)
                            
                            print(f"\nSuccessor for {self.current_dictator.name}:")
                            print(successor)
                            
                            # Transition to one-party state
                            print(f"\n   Regime transitions to ONE-PARTY STATE")
                            print(f"   Ruling party: {self.regime_party.name}")
                            self.regime_type = 'one_party'
                            self.current_dictator = None
                            
                            # Schedule next election when successor's term ends
                            self.scheduled_election_year = successor.term_end
                            
                            # Continue revolution checks - jump to next 4-year interval
                            years_since_regime = year - self.regime_start_year
                            years_to_next_check = 4 - (years_since_regime % 4) if years_since_regime % 4 != 0 else 4
                            next_election_year = year + years_to_next_check
                            continue
                    else:
                        # Dictator still alive, advance time
                        # BUT: check if dictator will die before the next 4-year revolution check
                        # Calculate next revolution check year (must be divisible by 4 from regime_start)
                        years_since_regime = year - self.regime_start_year
                        years_to_next_check = 4 - (years_since_regime % 4) if years_since_regime % 4 != 0 else 4
                        next_revolution_check = year + years_to_next_check
                        
                        if self.current_dictator and self.current_dictator.final_death_year < next_revolution_check:
                            # Dictator will die before next check - jump to death year
                            next_election_year = self.current_dictator.final_death_year
                        else:
                            # Jump to next revolution check
                            next_election_year = next_revolution_check
                        continue
                elif self.regime_type == 'one_party':
                    # For one-party states, check if it's time for an election
                    if self.scheduled_election_year is None or year >= self.scheduled_election_year:
                        # Time for an election - fall through
                        pass
                    else:
                        # Not time for election yet
                        # Calculate next revolution check year (must be divisible by 4 from regime_start)
                        years_since_regime = year - self.regime_start_year
                        years_to_next_check = 4 - (years_since_regime % 4) if years_since_regime % 4 != 0 else 4
                        next_revolution_check = year + years_to_next_check
                        
                        # Check if the scheduled election happens before the next revolution check
                        if self.scheduled_election_year < next_revolution_check:
                            # Election happens before next revolution check - jump to election year
                            next_election_year = self.scheduled_election_year
                        else:
                            # Advance to next revolution check
                            next_election_year = next_revolution_check
                        continue

            # Normal election procedures (or one-party elections)
            if not self.is_authoritarian or self.regime_type == 'one_party':
                # Check for new party formation (only if not in authoritarian regime)
                if year >= 1792 and not self.is_authoritarian:
                    self.check_new_party_formation(year)

                # Shift party politics
                if year >= 1792:
                    self.shift_party_politics()

                    # Display current party political positions
                    active_parties_display = [p for p in self.parties if not p.dissolved]
                    if active_parties_display:
                        print(f"\nCurrent party positions for {year} election:")
                        for party in active_parties_display:
                            print(f"  {party}")

                # Check party mergers (only if not authoritarian)
                if year >= 1792 and not self.is_authoritarian:
                    self.check_party_mergers(year)

                # Check party dissolutions (only if not authoritarian)
                if year >= 1792 and not self.is_authoritarian:
                    self.check_party_dissolutions(year)

                # Select a party
                active_parties = [p for p in self.parties if not p.dissolved]
                if not active_parties:
                    # If no active parties, create one
                    new_party = Party.generate_new_party(year)
                    self.parties.append(new_party)
                    active_parties = [new_party]
                    print(f"\nEmergency party formed: {new_party}")

                # In one-party state, can only select the regime party
                if self.regime_type == 'one_party':
                    selected_party = self.regime_party
                else:
                    selected_party = random.choice(active_parties)

                # Check if we're at a scheduled election or just generating a president
                # For regular democracies, always generate. For one-party, check schedule.
                should_hold_election = True
                if self.regime_type == 'one_party':
                    if self.scheduled_election_year is not None and year < self.scheduled_election_year:
                        should_hold_election = False

                if should_hold_election:
                    # Check if there's a sitting president who should attempt term extension first
                    sitting_president = self.presidents[-1] if len(self.presidents) > 0 else None
                    president_got_extension = False

                    if (sitting_president and
                        sitting_president.num_terms == 2 and
                        not sitting_president.dies_in_office and
                        not revolution_succeeded and
                        not hasattr(sitting_president, 'extension_checked')):

                        sitting_president.extension_checked = True
                        got_third, got_fourth, auth_type = self.attempt_term_extension(sitting_president, sitting_president.term_end)

                        if got_third or got_fourth:
                            president_got_extension = True

                            # Handle authoritarian takeover if got 4th term
                            if got_fourth and auth_type:
                                if self.attempt_authoritarian_takeover(sitting_president, auth_type):
                                    # For dictatorships/hybrids, check if dictator will die before next revolution check
                                    if auth_type in ['dictatorship', 'hybrid'] and sitting_president.final_death_year < sitting_president.completed_term_end + 4:
                                        # Dictator will be assassinated before next revolution check
                                        next_election_year = sitting_president.final_death_year
                                    else:
                                        # Jump to next revolution check (4 years after takeover)
                                        next_election_year = sitting_president.completed_term_end + 4
                                    continue

                            # Set next election to when extended term ends
                            if self.regime_type == 'one_party':
                                self.scheduled_election_year = sitting_president.completed_term_end
                                next_election_year = year + 4
                            else:
                                next_election_year = sitting_president.completed_term_end

                            # Handle death during extended term
                            if sitting_president.dies_in_office:
                                successor = self.generate_successor(sitting_president)
                                sitting_president.successor = successor
                                self.presidents.append(successor)
                                if self.regime_type == 'one_party':
                                    self.scheduled_election_year = successor.term_end
                                    next_election_year = year + 4
                                else:
                                    next_election_year = successor.term_end
                                print(f"\nSuccessor for {sitting_president.name}:")
                                print(successor)

                            continue

                    # Generate new president if sitting one didn't get extension
                    if not president_got_extension:
                        print(f"\nGenerating president for {year} election...")
                        president = self.generate_president(year, selected_party)
                        self.presidents.append(president)
                        print(president)

                # Next election happens in the year the term ends
                # For one-party states, we need to handle this differently
                if self.regime_type == 'one_party':
                    # Get the last president (could be extended prev_president or new president)
                    last_president = self.presidents[-1]
                    # Schedule the actual election
                    self.scheduled_election_year = last_president.completed_term_end
                    # But we always advance by 4 years for revolution checks
                    next_election_year = year + 4
                else:
                    # Normal democracy
                    last_president = self.presidents[-1]
                    next_election_year = last_president.completed_term_end

                # Handle successor if president dies
                last_president = self.presidents[-1]
                if last_president.dies_in_office:
                    successor = self.generate_successor(last_president)
                    last_president.successor = successor
                    self.presidents.append(successor)
                    if self.regime_type == 'one_party':
                        self.scheduled_election_year = successor.term_end
                        next_election_year = year + 4
                    else:
                        next_election_year = successor.term_end
                    print(f"\nSuccessor for {last_president.name}:")
                    print(successor)

                    # Check if successor should attempt term extensions (if they got 2 full elected terms and no revolution)
                    if successor.num_terms == 2 and not revolution_succeeded:
                        got_third_succ, got_fourth_succ, auth_type_succ = self.attempt_term_extension(successor, successor.term_end)
                        if got_fourth_succ and auth_type_succ:
                            if not self.attempt_authoritarian_takeover(successor, auth_type_succ):
                                # Takeover failed
                                pass
                        # Update next election year if successor got extensions
                        next_election_year = successor.term_end

        # Print summary
        self.print_summary()

    def print_summary(self):
        """Print a summary of the alternate history"""
        print("\n" + "="*80)
        print("SUMMARY")
        print("="*80)
        print(f"\nTotal presidents generated: {len(self.presidents)}")
        print(f"Total parties ever formed: {len(self.parties)}")

        active_parties = [p for p in self.parties if not p.dissolved]
        print(f"Active parties at end: {len(active_parties)}")

        deaths_in_office = sum(1 for p in self.presidents if p.dies_in_office)
        assassinations = sum(1 for p in self.presidents if p.dies_in_office and p.death_cause == "Assassination")
        natural_deaths = sum(1 for p in self.presidents if p.dies_in_office and p.death_cause == "Natural Causes")

        print(f"\nPresidents who died in office: {deaths_in_office}")
        print(f"  - Assassinations: {assassinations}")
        print(f"  - Natural causes: {natural_deaths}")

        female_presidents = sum(1 for p in self.presidents if p.gender == "Female")
        print(f"\nFemale presidents: {female_presidents}")

        print("\nActive parties at end of simulation:")
        for party in active_parties:
            years_active = 2024 - party.founding_year
            print(f"  {party} - Founded {party.founding_year} ({years_active} years)")


def main():
    """Main entry point"""
    print("\nStarting Alternate US Presidential History Generator...\n")

    generator = AlternateHistoryGenerator()
    generator.run_simulation()

    print("\n" + "="*80)
    print("Simulation complete!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
