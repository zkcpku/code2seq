#!/usr/bin/env bash

data_dir=Python150kExtractor/processed
data_name=$(basename "${data_dir}")
data=${data_dir}/${data_name}
test=${data_dir}/${data_name}.val.c2s
run_name=default
model_dir=models/python150k-${run_name}
save_prefix=${model_dir}/model
cuda=2
seed=239

mkdir -p "${model_dir}"
set -e
export CUDA_VISIBLE_DEVICES=2
nohup python -u code2seq.py \
  --data="${data}" \
  --test="${test}" \
  --save_prefix="${save_prefix}" \
  --seed="${seed}" > py150_train.log 2>&1 &