import get_data
import consolidate_data
import topic_modeling
import scrub_data
import analyze_data
import visualize_data

if __name__ == '__main__':
    # 1. download data (warning, may take several minutes)
    # get_data.get_data()
    
    # 2. process data
    consolidate_data.consolidate_indorecipes_data()
    topic_modeling.generate_topics()
    scrub_data.scrub_ubereats_data() # may take a minute
    consolidate_data.consolidate_ubereats_data()

    # 3. analyze data
    analyze_data.analyze_data()
    visualize_data.visualize_data()
