from model import mem_transformer
from argparse import ArgumentParser
import os
import sys
import torch
from torchsummary import summary
from utils import TxlSimpleSampler, load_vocab

def get_parser():
	parser = ArgumentParser()

	parser.add_argument('model_dir', type=str, help='Directory with model')
	parser.add_argument('--tx2', action='store_false', dest='tx1')
	parser.add_argument('--out_dir', type=str, help='Output directory')
	parser.add_argument('--cpu', action='store_false', dest='gpu')
	parser.add_argument('--num', type=int, help='Number of samples to generate')
	parser.add_argument('--mem_len', type=int, help='Max length of Transformer memory')
	parser.add_argument('--gen_len', type=int, help='Length of generation')
	parser.add_argument('--temp', type=float, help='Generation temperature')
	parser.add_argument('--topk', type=int, help='Top-k sampling')

	parser.set_defaults(
		model_dir='./model',
		tx1=True,
		out_dir='./',
		gpu=True,
		num=1,
		mem_len=512,
		gen_len=1024,
		temp=0.95,
		topk=32)

	return parser

if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()
	model_fp = os.path.join(args.model_dir, 'model.pt')
	vocab_fp = os.path.join(args.model_dir, 'vocab.txt')
	if not os.path.isdir(args.out_dir):
		os.makedirs(args.out_dir)
	ext = '.tx1.txt' if args.tx1 else '.tx2.txt'
	device = torch.device('cuda' if args.gpu else 'cpu')

	# Load the best saved model.
	with open(model_fp, 'rb') as f:
		model = torch.load(f)
	model.backward_compatible()
	model = model.to(device)

	for p in model.parameters():
		print(p.numel())

	summary(model, (512,))


