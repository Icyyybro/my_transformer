import torch
import torch.nn.functional as F
from torch import nn
import math
import copy


class EncoderDecoder(nn.Module):
    def __init__(self, encoder, decoder, source_embed, target_embed, generator):
        super(EncoderDecoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = source_embed
        self.tgt_embed = target_embed
        self.generator = generator

    def encode(self, source, source_mask):
        return self.encoder(self.src_embed(source), source_mask)

    def decode(self, memory, source_mask, target, target_mask):
        return self.decoder(self.tgt_embed(target), memory, source_mask, target_mask)

    def forward(self, source, target, source_mask, target_mask):
        # source: 代表源数据
        # target: 代表目标数据
        return self.decode(self.encode(source, source_mask), source_mask, target, target_mask)