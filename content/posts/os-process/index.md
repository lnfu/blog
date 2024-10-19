+++
title = '作業系統 - Process'
date = 2024-10-19T17:21:05+08:00
draft = false
tags = ['Operating System']
+++

行程 (process): active program (執行中的應用程式) and related resources, such as process state, memory address space.

執行緒 (thread): lightweight process, thread 之間共享同一個 memory address space

對於 Linux 來說, PCB (process control block) = process descriptor = `tast_struct`

此外, Linux 對於 thread 使用同樣的資料結構 `tast_struct`

`thread_info` 資料結構位於 kernel stack (kernel stack 大小通常是 2 -3 pages) 的底部, 可以透過 `current_thread_info()` 找到得到指向 `thread_info`  的指標 (pointer), 然後去查看 `thread_info` 裡面指向 `task_struct` 的指標

5 種 state:

1. `Task_Running`
2. `Task_Interruptible`
3. `Task_Uniterruptible`
4. `__Task_Stopped`
5. `__Task_Traced`

pid = 1 的行程是 `init`

## 建立行程 (Process Creation)

使用者呼叫: `fork()` + `exec()`

Copy-on-Write (COW): 每次建立 (複製) process 的時候, 如果都把所有 parent process 的資料完整複製會太耗費時間, 所以改成在建立時讓 parent 和 child 的 page table 中每個 entry 的 virtual memory address 都指向同一位置, 只有當對資料有做修改時才會透過中斷, 把要寫入資料的 page 真正複製出來 (仍然只複製有寫入的 page)

實際上是透過 `copy_process()` 實作:

- 分配新的 kernel stack (包含 `thread_info`), 新的 `task_struct`, 設定好 child 的 PID
- 複製 parent 的 page table
- 複製 open files, file system 等資料

## 建立執行緒 (Thread Creation)

使用者呼叫: `clone()`

## 排程 (Scheduling)

個人認為作業系統在 process 最重要的就是排程, 而在 memory 最重要的就是 paging

### Criteria

scheduling criteria 指的就是我們應該在設計排程演算法時候應該考量到的指標

大致可以分成 3 類

- should be minimized (越小越好)
  - response time
  - turnaround time
- should be maximized (越大越好)
  - CPU utilization
  - throughput
- 其他
  - fairness
  - starvation
  - preemtive (vs. cooperative)

### Linux 的排程

Linux 排程算法的歷史大致可以分成三個階段 (還可以追溯更早的, 不過我們就先以這三個做討論)

O(N)

O(N) 主要有兩個問題:

1. 每次排程時都要花費 O(N) 太慢
2. 所有 CPUs (cores) 共用同一個 global runqueue, 因此在存取這個 runqueue 時就必須先 lock, 存取完成再 unlock 以達到 mutex (互斥)

O(1)

使用 140-bit bitmap 加上相關的指令 (找出 leading bit) 來達到 O(1) 時間就能夠找到對應的 queue (總共有 140 queues)

100 是給 realtime process (Linux 只提供 soft realtime), SCHED_FIFO, SCHED_RR

40 給 normal process

O(1) 會有的問題:

1. nice value 大 (優先級小) 的 process 可能會面臨 starvation (interactive 差)
2. 如果目前在 runqueue 的所有 process 的 nice value 都很大 (優先級小 e.g., nice value = 19, time slice = 5ms), 會造成非常頻繁的 context switch
3. time slice 的差異在不同段位下分佈非常不平均, 例如 nice value = -20 的 time slice (800ms) 相比 nice value = -19 的 time slice (780ms) 多 20 (1.03 倍左右), 但是 nice value = 18 的 time slice (10ms) 卻是 nice value = 19 的 time slice (5ms) 的兩倍

CFS

引入 vruntime 的概念 (考慮 priority 後, CPU 會認為目前 process 已經執行的時間)

vruntime = delta_exec * NICE_Weight/NICE_k_Weight

## Context Switch

context:

1. user address space (e.g., page table)
2. registers (e.g., PC)
3. kernel data structures that relate to the process

context switch: switching from one runnable process to another

會做什麼? store the context of the current process, restore the context of the next context

- switch_mm(): switch the *virtual memory mapping* (包含 flush branch prediction table, 讀取 page table, flush TLB)
- switch_to(): switch the *process state* (e.g., register)

比較麻煩的是, 對於 interrupt (or exception), CPU 會做類似 context switch (也就是 interrupt context) 然後執行 kernel code, 但是和我們普遍認知的 (process level) context switch 不太一樣

## System Call

system call 提供了 user space 程式一個界面 (interface) 來和作業系統進行互動 (interaction)

Brief Procedures (Details: See References):
Write a new system call (e.g., sys_hello.c)
Create a Makefile
Add the new system call into the system call table
Parameters: System_call_number, arch(e.g., 64), system_call_name,  program_of_system_call
Add the new system call to the header file (include/linux/syscalls.h)
Compile/Install/Update Kernel   
