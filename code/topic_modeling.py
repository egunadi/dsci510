import little_mallet_wrapper
import seaborn
import pandas as pd
from pathlib import Path

def generate_topics():
    path_to_mallet = '../mallet-2.0.8/bin/mallet'

    indofoods_df = pd.read_csv('../data/indofoods.csv', encoding='utf-8')

    training_data = [   little_mallet_wrapper.process_string(text, numbers='remove')
                        for text in indofoods_df['Title']   ]

    original_dishnames = [  title
                            for title in indofoods_df['Title']  ]

    # little_mallet_wrapper.print_dataset_stats(training_data)
    # OUTPUT
    """
    Number of Documents: 15641
    Mean Number of Words per Document: 3.8
    Vocabulary Size: 3525
    """

    num_topics = 25
    training_data = training_data
    output_directory_path = '../result/indofoods'

    Path(f"{output_directory_path}").mkdir(parents=True, exist_ok=True)

    path_to_training_data           = f"{output_directory_path}/training.txt"
    path_to_formatted_training_data = f"{output_directory_path}/mallet.training"
    path_to_model                   = f"{output_directory_path}/mallet.model.{str(num_topics)}"
    path_to_topic_keys              = f"{output_directory_path}/mallet.topic_keys.{str(num_topics)}"
    path_to_topic_distributions     = f"{output_directory_path}/mallet.topic_distributions.{str(num_topics)}"

    little_mallet_wrapper.quick_train_topic_model(  path_to_mallet,
                                                    output_directory_path,
                                                    num_topics,
                                                    training_data   )

    topics = little_mallet_wrapper.load_topic_keys(path_to_topic_keys)

    topic_distributions = little_mallet_wrapper.load_topic_distributions(path_to_topic_distributions)

    training_data_dishnames = dict(zip(training_data, original_dishnames))

    def display_top_titles_per_topic(topic_number=0, number_of_documents=5):
        output = f"✨Topic {topic_number}✨\n\n{topics[topic_number]}\n"

        for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents):
            output = output + " " + str(round(probability, 4)) + " " + training_data_dishnames[document] + "\n"
        
        return output

    with open('../result/indofoods_topics.txt', 'w') as contents:
        contents.write(display_top_titles_per_topic(topic_number=0, number_of_documents=5))
    
    with open('../result/indofoods_topics.txt', 'a') as contents:
        for number in range(1, 25):
            contents.write('\n')
            contents.write(display_top_titles_per_topic(topic_number=number, number_of_documents=5))

if __name__ == '__main__':
    generate_topics()
