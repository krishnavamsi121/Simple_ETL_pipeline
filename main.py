from src import extract, transform, load

if __name__ == '__main__':
    filepath = "C:/Users/vamsi/spotify_analysis/pipeline_template_assessment/data/rapcaviar_raw.csv"
    df_raw = extract.extract_data(filepath)
    df_trans = transform.transform_data(df_raw)
    load.load_data(df_trans)
