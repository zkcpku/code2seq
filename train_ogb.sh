#!/usr/bin/env bash

data_dir=ogb_python/new_processed/
data_name=$(basename "${data_dir}")
data=${data_dir}/${data_name}
test=${data_dir}/${data_name}.val.c2s
run_name=default
model_dir=models/ogb_127_new-${run_name}
save_prefix=${model_dir}/model
cuda=1
seed=239

mkdir -p "${model_dir}"
set -e
export CUDA_VISIBLE_DEVICES=$cuda
nohup  python -u code2seq.py \
  --data="${data}" \
  --test="${test}" \
  --save_prefix="${save_prefix}" \
  --seed="${seed}" > my_127_new_ogb.log 2>&1 &
