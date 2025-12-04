# run_demo.py
import networkx as nx
import random
import logging

from Network_Useful_Function import (
    all_shortest_from,
    snowball_sampling,
    snowball_sampling_shuffle,
    modularity,
    STOPWORDS,
    get_word_frequencies_from_all_course_descriptions,
    get_course_titles_and_descriptions,
    get_people_in_article,
    collect_people_from_random_articles
)

logging.basicConfig(level=logging.INFO)

def demo_graph_utils():
    print("=== Graph Utils Demo ===")
    G = nx.Graph()
    G.add_edges_from([(1,2),(2,3),(3,4),(4,5)])
    print("All shortest paths from node 1:")
    distances = all_shortest_from(G, 1)
    print(distances)

    communities = [{1,2,3}, {4,5}]
    Q = modularity(G, communities)
    print(f"Modularity score: {Q}\n")

def demo_snowball_sampling():
    print("=== Snowball Sampling Demo ===")
    G = nx.path_graph(10)
    seeds = [0]
    sampled1 = snowball_sampling(G, seeds, size=5, max_wave=2)
    sampled2 = snowball_sampling_shuffle(G, seeds, size=5, max_wave=2)
    print(f"Snowball sampled nodes: {sampled1}")
    print(f"Shuffled snowball sampled nodes: {sampled2}\n")

def demo_text_analysis():
    print("=== Text Analysis Demo ===")
    descriptions = [
        "This is a test course.",
        "Test the course and test again."
    ]
    freqs = get_word_frequencies_from_all_course_descriptions(descriptions)
    print("Word frequencies (excluding stopwords):")
    for word, count in freqs:
        print(f"{word}: {count}")
    print()

def demo_course_scraper():
    print("=== Course Scraper Demo ===")
    # 你可以改成可访问的课程网页
    url = "https://catalog.northeastern.edu/course-descriptions/eece/"
    try:
        courses = get_course_titles_and_descriptions(url)
        for title, desc in list(courses.items())[:5]:  # 只显示前5条
            print(f"{title}: {desc}")
    except Exception as e:
        print(f"Failed to scrape courses: {e}")
    print()

def demo_people_scraper():
    print("=== People in Article Demo ===")
    # 用示例 URL 或 collect_people_from_random_articles
    try:
        # collect 3 random articles from a CSV (示例)
        people_lists = collect_people_from_random_articles(sample_size=3)
        print("People collected from random articles:")
        for lst in people_lists:
            print(lst)
    except Exception as e:
        print(f"Failed to scrape people: {e}")
    print()

if __name__ == "__main__":
    demo_graph_utils()
    demo_snowball_sampling()
    demo_text_analysis()
    demo_course_scraper()
    demo_people_scraper()
