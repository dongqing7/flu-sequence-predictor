from Bio import SeqIO
import pandas as pd
import logging


logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)


def load_sequence_and_metadata():
    """
    Returns the sequences as a list of SeqRecords, and metadata as a pandas
    DataFrame.
    """
    logger.debug('started load_sequence_and_metadata()')
    sequences = [s for s in SeqIO.parse('data/20170531-H3N2-global.fasta',
                                        'fasta')]
    metadata = pd.read_csv('data/20170531-H3N2-global.tsv', sep='\t',
                           parse_dates=['Collection Date'])
    logger.debug('finished load_sequence_and_metadata()')
    return sequences, metadata


def load_prediction_coordinates():
    """
    Returns the coordinates of the predictions, and their associated colours,
    as a pandas DataFrame.
    """
    logger.debug('started load_prediction_coordinates()')
    df = pd.read_csv('data/oneQ_prediction_coords_with_colors.csv', index_col=0)
    logger.debug('finished load_prediction_coordinates()')
    return df
