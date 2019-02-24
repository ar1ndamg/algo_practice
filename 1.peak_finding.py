def find_peak(array, rows, start,end):

    mid_col = start + (end-start)//2
    max_row_index, max_val = find_1d_peak(array, mid_col,0,rows-1)
    # max_val = array[0][mid_col]
    # max_row_index = 0

    # for i in range(1,rows):
    #     if array[i][mid_col] > max_val:
    #         max_val = array[i][mid_col]
    #         max_row_index = i
    print(f"start: {start} end: {end} middle: {mid_col} max_val: {max_val} max index: {max_row_index}")
    right = array[max_row_index][mid_col+1]
    left = array[max_row_index][mid_col-1]
    if max_val < left and left >= right :
        print("going left")
        return find_peak(array,rows, start, mid_col-1)
    elif right > max_val :
        print("going right")
        return find_peak(array, rows, mid_col+1, end)
    else:
        return max_val, max_row_index, mid_col

def find_1d_peak(arr,col,start,end):
    mid = start + (end-start)//2
    mid_val = arr[mid][col]
    if mid_val < arr[mid+1][col]:
        return find_1d_peak(arr,col,mid+1,end)
    elif mid_val < arr[mid-1][col]:
        return find_1d_peak(arr, col, start, mid-1)
    else:
        return mid,mid_val

if __name__ == '__main__':
    matrix = [
        [10,1,1,4],
        [5,4,2,15],
        [14,7,16,6],
        [15,2,9,12]
    ]
    print(find_peak(matrix,4,0,3))