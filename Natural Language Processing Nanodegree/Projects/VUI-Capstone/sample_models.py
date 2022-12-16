from tensorflow.keras import backend as K
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import (BatchNormalization, Conv1D, Dense, Input,
    TimeDistributed, Activation, Bidirectional, SimpleRNN, GRU, LSTM)

def simple_rnn_model(input_dim, output_dim=29):
    """ Build a recurrent network for speech
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # Add recurrent layer
    simp_rnn = GRU(output_dim, return_sequences=True,
                name='rnn')(input_data)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(simp_rnn)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model

def rnn_model(input_dim, units, activation, output_dim=29):
    """ Build a recurrent network for speech
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # Add recurrent layer
    simp_rnn = GRU(units, activation=activation,
        return_sequences=True,  name='rnn')(input_data)
    # TODO: Add batch normalization
    bn_rnn = BatchNormalization(name='bn_rnn')(simp_rnn)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model


def cnn_rnn_model(input_dim, filters, kernel_size, conv_stride,
    conv_border_mode, units, output_dim=29):
    """ Build a recurrent + convolutional network for speech
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # Add convolutional layer
    conv_1d = Conv1D(filters, kernel_size,
                    strides=conv_stride,
                    padding=conv_border_mode,
                    activation='relu',
                    name='conv1d')(input_data)
    # Add batch normalization
    bn_cnn = BatchNormalization(name='bn_conv_1d')(conv_1d)
    # Add a recurrent layer
    simp_rnn = SimpleRNN(units, activation='tanh',
        return_sequences=True,  name='rnn')(bn_cnn)
    # TODO: Add batch normalization
    bn_rnn = BatchNormalization(name='bn_rnn')(simp_rnn)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: cnn_output_length(
        x, kernel_size, conv_border_mode, conv_stride)
    print(model.summary())
    return model

def cnn_output_length(input_length, filter_size, border_mode, stride,
                    dilation=1):
    """ Compute the length of the output sequence after 1D convolution along
        time. Note that this function is in line with the function used in
        Convolution1D class from Keras.
    Params:
        input_length (int): Length of the input sequence.
        filter_size (int): Width of the convolution kernel.
        border_mode (str): Only support `same` or `valid`.
        stride (int): Stride size used in 1D convolution.
        dilation (int)
    """
    if input_length is None:
        return None
    assert border_mode in {'same', 'valid'}
    dilated_filter_size = filter_size + (filter_size - 1) * (dilation - 1)
    if border_mode == 'same':
        output_length = input_length
    elif border_mode == 'valid':
        output_length = input_length - dilated_filter_size + 1
    return (output_length + stride - 1) // stride

def deep_rnn_model(input_dim, units, recur_layers, output_dim=29):
    """ Build a deep recurrent network for speech
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # TODO: Add recurrent layers, each with batch normalization
    for i in range(recur_layers):
        simp_rnn = GRU(units, activation='tanh', return_sequences=True,
            name=f'rnn_{i}')(input_data)
        bn_rnn = BatchNormalization(name=f'bn_rnn_{i}')(simp_rnn)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model

def bidirectional_rnn_model(input_dim, units, output_dim=29):
    """ Build a bidirectional recurrent network for speech
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    # TODO: Add bidirectional recurrent layer
    bidir_rnn = Bidirectional(GRU(units, activation='tanh', return_sequences=True,  name='bidir_rnn'))(input_data)
    # TODO: Add a TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(bidir_rnn)
    # Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x
    print(model.summary())
    return model

def final_model(input_dim, units, recur_layers, output_dim=29):
    """ Build a deep network for speech 
    """
    # Main acoustic input
    input_data = Input(name='the_input', shape=(None, input_dim))
    
    # Add convolutional layer
    conv_1d_1 = Conv1D(filters=250, kernel_size=11, 
                         strides=2, 
                         padding='same',
                         activation='elu',
                         name='conv1d_1')(input_data)
    bn_cnn_1 = BatchNormalization(name='bn_conv_1d')(conv_1d_1)
#     conv_1d_2 = Conv1D(filters=300, kernel_size=7, 
#                      strides=2, 
#                      padding='same',
#                      activation='elu',
#                      name='conv1d_2')(bn_cnn_1)
#     bn_cnn_2 = BatchNormalization(name='bn_conv_2d')(conv_1d_2)
    
    # Add recurrent layers, each with batch normalization
    for i in range(recur_layers):
        if i == 0:
            cur_input = bn_cnn_1
        else:
            cur_input = deep_rnn
        deep_rnn = Bidirectional(GRU(units, activation='tanh', return_sequences=True,
            name=f"rnn_{i}", dropout=0.2))(cur_input)
        deep_rnn = BatchNormalization(name=f"bn_rnn_{i}")(deep_rnn)
    
    # TimeDistributed(Dense(output_dim)) layer
    time_dense = TimeDistributed(Dense(output_dim))(deep_rnn)
    # TODO: Add softmax activation layer
    y_pred = Activation('softmax', name='softmax')(time_dense)
    # Specify the model
    model = Model(inputs=input_data, outputs=y_pred)
    # TODO: Specify model.output_length
    model.output_length = lambda x: cnn_output_length(x, 11, 'same', 2)
    print(model.summary())
    return model
    
    # C2  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\...
    # \  /  \  /  \  /  \  /  \  /  \  /  \
    #     /    \      /    \      /    \
    # C1  /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\  /\ /...\
    # X: 0  1  2  3  4  5  6  7  8  9  10 11 12 ... 111
    # Y: 1  2  3  4  5  6  7  8  9  10 11 12 13 ... 112
    #  /14 15 16 17 18 19 20 21 22  23 24 25 26 ... 125
    # model = Sequential()
    # model.add(Input(input_shape=[None, input_dim]))
    # for rate in (1, 2, 4, 8) * 2:
    #     model.add(Conv1D(filters, kernel_size,
    #                      strides=conv_stride,
    #                      padding=conv_border_mode,
    #                      activation='relu',
    #                      dilation_rate=rate))
    # model.add(Conv1D(filters=output_dim, kernel_size=1))
    # model.output_length = lambda x: cnn_output_length(x, kernel_size, conv_border_mode, conv_stride)
