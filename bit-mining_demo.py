import time
from hashlib import sha256

start_time = time.perf_counter()

nonce = 1000000000
block_1 = """
	sunday -> mike = 20
	stephen -> susan = 40
	eks -> swim = 3
	track -> plot = 127
	me -> wenst	= 1909
"""
prev_hash = '0000008345e8d1d6ef68fbbd0dadee2d8be4bcc2718fa3311ead47db7a396106'

for n in range(nonce):
	now_hash = sha256(str.encode(str(n)) + str.encode(block_1) + str.encode(prev_hash)).hexdigest()
	if now_hash.startswith("000000"):
		print(now_hash, "\t",n, "\t",(time.perf_counter()-start_time)/60)


end_time = time.perf_counter() - start_time

print(end_time/60)