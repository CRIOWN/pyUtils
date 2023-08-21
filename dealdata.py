import threading

BLOCK_SIZE = 1000000  # 每个块的大小，根据需要进行调整
NUM_THREADS = 4  # 并行处理的线程数，根据需要进行调整

def process_block(block_lines):
    lines_seen = set()
    output_lines = []

    for line in block_lines:
        if line not in lines_seen:
            lines_seen.add(line)
            output_lines.append(line)

    return output_lines

def process_file(filename):
    all_blocks = []

    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            block_lines = file.readlines(BLOCK_SIZE)
            if not block_lines:
                break

            all_blocks.append(block_lines)

    num_blocks = len(all_blocks)

    threads = []
    results = [[] for _ in range(num_blocks)]

    for i in range(num_blocks):
        block_lines = all_blocks[i]

        thread = threading.Thread(target=lambda idx, lines: results[idx].extend(process_block(lines)), args=(i, block_lines))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # 合并结果
    output_lines = [line for sublist in results for line in sublist]
    # 写入到文件
    with open('data_done.txt', 'w') as output_file:
        output_file.writelines(output_lines)


if __name__ == '__main__':
    filename = 'data.20230617.txt'
    process_file(filename)