BLOCK_SIZE = 100000  # 每个块的大小，根据需要进行调整
NUM_BLOCKS = 10  # 分块的数量，根据需要进行调整

def process_block(block_lines, block_num):
    # 处理数据块的逻辑
    output_lines = []

    for line in block_lines:
        output_lines.append(line)

    # 写入到文件
    with open(f'data_{block_num}.txt', 'w') as output_file:
        output_file.writelines(output_lines)

def process_file(filename):
    with open(filename, 'r') as file:
        all_lines = file.readlines()

    lines_per_block = len(all_lines) // NUM_BLOCKS

    for i in range(NUM_BLOCKS):
        start_idx = i * lines_per_block
        end_idx = start_idx + lines_per_block
        if i == NUM_BLOCKS - 1:
            # 处理最后一个块，包含剩余的行
            block_lines = all_lines[start_idx:]
        else:
            block_lines = all_lines[start_idx:end_idx]

        process_block(block_lines, i)


if __name__ == '__main__':
    filename = 'data_done.txt'
    process_file(filename)