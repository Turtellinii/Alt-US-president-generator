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
    target_combos = ['ENTJ 3w4 ', 'ESTJ 3w4 ', 'ESTP 3w4 ']
    for combo in target_combos:
        if combo in president.personality:
            reasons_met.append(2)
            break

    # Condition 3: President's social score >= 67
    if president.social_score >= 67:
        reasons_met.append(3)

    # Condition 4: Party's social score >= 67 (if they have a party)
    if president.party and president.party.social_score >= 67:
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

    def __init__(self, election_year, party=None, is_successor=False, is_first_president=False):
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
            # Clamp to -100 to 100 range
            personal_social = random.randint(-25, 25)
            personal_economic = random.randint(-25, 25)
            self.social_score = max(-100, min(100, party.social_score + personal_social))
            self.economic_score = max(-100, min(100, party.economic_score + personal_economic))

        # Generate life years
        # Birth year: election year - random(35-70)
        age_at_election = random.randint(35, 70)
        self.birth_year = election_year - age_at_election

        # Death year based on era
        if election_year < 1800:
            lifespan = random.randint(60, 80)
        elif election_year < 1851:
            lifespan = random.randint(60, 85)
        elif election_year < 1900:
            lifespan = random.randint(65, 90)
        elif election_year < 1951:
            lifespan = random.randint(65, 95)
        elif election_year < 2001:
            lifespan = random.randint(70, 100)
        else:
            lifespan = random.randint(70, 105)

        natural_death_year = self.birth_year + lifespan

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
        self.revolution_success_chance = 20  # Starts at 20%
        self.years_since_regime_check = 0

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

    def generate_president(self, year, party=None, is_successor=False, is_first_president=False):
        """Generate a new president"""
        president = President(year, party, is_successor, is_first_president)

        # Update party's last_in_power
        if party:
            party.last_in_power = year

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

        return successor

    def attempt_term_extension(self, president):
        """Handle president attempting 3rd and 4th terms

        Returns tuple: (got_third_term, got_fourth_term, authoritarian_type)
        """
        attempts, reasons = check_authoritarian_tendency(president)

        if not attempts:
            return False, False, None

        print(f"\n⚠️  {president.name} attempts to run for a THIRD TERM!")
        print(f"   Reasons: {', '.join(['Enneagram 8w7/8w9' if 1 in reasons else '', 'MBTI combo' if 2 in reasons else '', 'High personal auth score' if 3 in reasons else '', 'High party auth score' if 4 in reasons else ''])}")

        # 50% chance of getting 3rd term
        if random.randint(1, 100) <= 50:
            print(f"   ✓ Third term GRANTED! ({president.term_end+1}-{president.term_end+4})")
            got_third = True
            president.num_terms = 3
            president.term_end += 4
            president.completed_term_end = president.term_end
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

            # Determine authoritarian type based on reasons
            if 3 in reasons and 4 in reasons:
                auth_type = 'hybrid'
            elif 4 in reasons:
                auth_type = 'one_party'
            elif 3 in reasons:
                auth_type = 'dictatorship'
            else:
                # Default to dictatorship if neither social score triggered it
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
            self.years_since_regime_check = 0

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
            print(f"   {president.party.name} has been ELIMINATED")

            # Eliminate the president's party
            president.party.dissolved = True

            return False

    def generate_family_successor(self, dictator):
        """Generate a family member to succeed a dictator"""
        # Same last name and state, but younger
        last_name = dictator.name.split()[1]
        first_name_era = get_name_era(dictator.death_year if dictator.dies_in_office else dictator.final_death_year)

        # Generate first name
        if dictator.gender == "Female" or random.randint(1, 2) == 1:
            first_name = random.choice(FIRST_NAMES_FEMALE[first_name_era])
        else:
            first_name = random.choice(FIRST_NAMES_MALE[first_name_era])

        # Create successor
        succession_year = dictator.death_year if dictator.dies_in_office else dictator.final_death_year
        successor = President(succession_year, dictator.party if dictator.party else None)

        # Override with family details
        successor.name = f"{first_name} {last_name}"
        successor.state = dictator.state
        successor.birth_year = dictator.birth_year + random.randint(20, 40)  # 20-40 years younger

        # Dictator rules until natural death
        successor.term_start = succession_year + 1
        successor.term_end = succession_year + 50  # Placeholder, will rule until death
        successor.num_terms = 999  # Special marker for dictator

        print(f"\n👑 New Dictator: {successor.name} (family member)")

        return successor

    def check_revolution(self, year):
        """Check for revolution attempt and potential success"""
        # Increment years and attempt chance every 4 years
        if self.years_since_regime_check % 4 == 0 and self.years_since_regime_check > 0:
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
                    self.revolution_success_chance = 20

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

        self.years_since_regime_check += 1
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
        got_third, got_fourth, auth_type = self.attempt_term_extension(first_president)

        # Next election happens in the year the term ends
        next_election_year = first_president.completed_term_end
        if first_president.dies_in_office:
            successor = self.generate_successor(first_president)
            first_president.successor = successor
            self.presidents.append(successor)
            next_election_year = successor.term_end
            print(f"\nSuccessor for {first_president.name}:")
            print(successor)

        # Handle authoritarian takeover if president got 4th term
        if got_fourth and auth_type:
            if not self.attempt_authoritarian_takeover(first_president, auth_type):
                # Takeover failed, hold special election
                print(f"\n🗳️  SPECIAL ELECTION held in {next_election_year}")

        # Initialize parties in 1792
        self.initialize_parties()

        # Continue elections until 2024
        while next_election_year <= 2024:
            year = next_election_year

            # Check for revolution if under authoritarian regime
            if self.is_authoritarian:
                if self.check_revolution(year):
                    # Revolution succeeded, hold special election
                    print(f"\n🗳️  SPECIAL ELECTION in {year}")
                elif self.regime_type in ['dictatorship', 'hybrid']:
                    # Under dictatorship, check if dictator dies
                    if self.current_dictator and year >= self.current_dictator.final_death_year:
                        print(f"\n💀 Dictator {self.current_dictator.name} has died")

                        if self.regime_type == 'dictatorship':
                            # Pure dictatorship: family succession
                            self.current_dictator = self.generate_family_successor(self.current_dictator)
                            self.presidents.append(self.current_dictator)
                            next_election_year = year + 4
                            continue
                        else:
                            # Hybrid: return to one-party elections
                            print(f"   Elections resume with {self.regime_party.name}")
                            self.regime_type = 'one_party'
                            self.current_dictator = None

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

                # Generate president
                print(f"\nGenerating president for {year} election...")
                president = self.generate_president(year, selected_party)
                self.presidents.append(president)
                print(president)

                # Check for term extension attempt (only if completed 2 terms)
                if president.num_terms == 2:
                    got_third, got_fourth, auth_type = self.attempt_term_extension(president)

                    # Handle authoritarian takeover if president got 4th term
                    if got_fourth and auth_type:
                        if not self.attempt_authoritarian_takeover(president, auth_type):
                            # Takeover failed, next election proceeds normally
                            pass

                # Next election happens in the year the term ends
                next_election_year = president.completed_term_end

                # Handle successor if president dies
                if president.dies_in_office:
                    successor = self.generate_successor(president)
                    president.successor = successor
                    self.presidents.append(successor)
                    next_election_year = successor.term_end
                    print(f"\nSuccessor for {president.name}:")
                    print(successor)

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
