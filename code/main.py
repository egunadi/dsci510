import get_data
import scrub_data
import consolidate_data
import analyze_data
import visualize_data

if __name__ == '__main__':
    # get_data.get_data()
    scrub_data.scrub_data()
    consolidate_data.consolidate_data()
    analyze_data.analyze_data()
    visualize_data.visualize_data()
