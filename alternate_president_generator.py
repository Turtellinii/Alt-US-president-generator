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

        social_score = random.randint(-100, 100)
        economic_score = random.randint(-100, 100)

        return cls(f"{color} Party", social_score, economic_score, year)

    def shift_politics(self):
        """Randomly shift party's political positions"""
        social_shift = random.randint(-20, 20)
        economic_shift = random.randint(-20, 20)

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
            # Die sometime during their term(s)
            self.death_year = random.randint(self.term_start, self.term_end)
            self.term_end = self.death_year

        # Generate political compass scores
        if party is None:
            # First president, no party
            self.social_score = random.randint(-100, 100)
            self.economic_score = random.randint(-100, 100)
        else:
            # Add individual variation to party scores
            personal_social = random.randint(-25, 25)
            personal_economic = random.randint(-25, 25)
            self.social_score = party.social_score + personal_social
            self.economic_score = party.economic_score + personal_economic

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

        # Next election happens in the year the term ends
        next_election_year = first_president.completed_term_end
        if first_president.dies_in_office:
            successor = self.generate_successor(first_president)
            first_president.successor = successor
            self.presidents.append(successor)
            # Next election is when the successor's term ends
            next_election_year = successor.term_end
            print(f"\nSuccessor for {first_president.name}:")
            print(successor)

        # Initialize parties in 1792
        self.initialize_parties()

        # Continue elections until 2024
        while next_election_year <= 2024:
            year = next_election_year

            # Check for new party formation
            if year >= 1792:
                self.check_new_party_formation(year)

            # Shift party politics
            if year >= 1792:
                self.shift_party_politics()

            # Check party dissolutions
            if year >= 1792:
                self.check_party_dissolutions(year)

            # Select a random active party
            active_parties = [p for p in self.parties if not p.dissolved]
            if not active_parties:
                # If no active parties, create one
                new_party = Party.generate_new_party(year)
                self.parties.append(new_party)
                active_parties = [new_party]
                print(f"\nEmergency party formed: {new_party}")

            selected_party = random.choice(active_parties)

            # Generate president
            print(f"\nGenerating president for {year} election...")
            president = self.generate_president(year, selected_party)
            self.presidents.append(president)
            print(president)

            # Next election happens in the year the term ends
            next_election_year = president.completed_term_end

            # Handle successor if president dies
            if president.dies_in_office:
                successor = self.generate_successor(president)
                president.successor = successor
                self.presidents.append(successor)
                # Next election is when the successor's term ends
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
