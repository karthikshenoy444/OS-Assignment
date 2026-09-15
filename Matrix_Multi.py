import random
import threading
import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 100
NUM_WORKERS = 8
MIN_DELAY = 0.04
MAX_DELAY = 0.18

mat_left = np.random.randint(1, 10, size=(N, N))
mat_right = np.random.randint(1, 10, size=(N, N))

mat_result = np.full((N, N), np.nan)

result_lock = threading.Lock()
rows_done = 0
last_row_finished = -1
finished = False


def compute_row(row_index):
    global rows_done, last_row_finished

    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

    row_values = mat_left[row_index, :] @ mat_right

    with result_lock:
        mat_result[row_index, :] = row_values
        rows_done += 1
        last_row_finished = row_index


def worker_loop(row_indices):
    global finished
    for r in row_indices:
        compute_row(r)
    with result_lock:
        if rows_done >= N:
            finished = True


row_order = list(range(N))
random.shuffle(row_order)
row_chunks = np.array_split(np.array(row_order), NUM_WORKERS)
threads = [threading.Thread(target=worker_loop, args=(chunk,), daemon=True)
           for chunk in row_chunks]

for t in threads:
    t.start()

plt.style.use("dark_background")

fig = plt.figure(figsize=(15, 6))
grid = fig.add_gridspec(2, 3, height_ratios=[10, 1])

ax_left = fig.add_subplot(grid[0, 0])
ax_right = fig.add_subplot(grid[0, 1])
ax_result = fig.add_subplot(grid[0, 2])
ax_progress = fig.add_subplot(grid[1, :])

ax_left.imshow(mat_left, cmap="cool")
ax_left.set_title("Left Matrix")

ax_right.imshow(mat_right, cmap="spring")
ax_right.set_title("Right Matrix")

for ax in (ax_left, ax_right, ax_result):
    ax.set_xticks([])
    ax.set_yticks([])

ax_result.set_title("Result Matrix (row-by-row)")

vmax_estimate = N * 9 * 9
img_result = ax_result.imshow(mat_result, cmap="turbo", vmin=0, vmax=vmax_estimate)

sweep_line = ax_result.axhline(y=-0.5, color="white", linewidth=2)

ax_progress.set_xlim(0, N)
ax_progress.set_ylim(0, 1)
ax_progress.set_xticks([])
ax_progress.set_yticks([])
progress_bar = ax_progress.barh(0.5, 0, height=1.0, color="deeppink")[0]
progress_label = ax_progress.text(
    N / 2, 0.5, "", ha="center", va="center", color="white", fontsize=11
)


def update(frame):
    with result_lock:
        current_done = rows_done
        current_row = last_row_finished
        snapshot = mat_result.copy()
        done_flag = finished

    img_result.set_data(snapshot)
    sweep_line.set_ydata([current_row - 0.5, current_row - 0.5])

    progress_bar.set_width(current_done)
    progress_label.set_text(f"{current_done}/{N} rows computed")

    if done_flag:
        anim.event_source.stop()

    return img_result, sweep_line, progress_bar, progress_label


anim = FuncAnimation(
    fig,
    update,
    interval=50,
    blit=False,
    cache_frame_data=False,
    save_count=500,
)

plt.tight_layout()
plt.show()
