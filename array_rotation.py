{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 4, 5, 1, 2]\n"
     ]
    }
   ],
   "source": [
    "# Program to rotate first d elements in an array\n",
    "\n",
    "def arr_rot(arr, d):\n",
    "    temp = []\n",
    "    arr_rot = []\n",
    "    for i in range(d):\n",
    "        temp.append(arr[0])\n",
    "        arr.pop(0)\n",
    "    arr_rot = arr + temp\n",
    "    print(arr_rot)\n",
    "        \n",
    "arr_rot([1,2,3,4,5], 2)\n",
    "\n",
    "'''\n",
    "In the above logic, total number of steps are \n",
    "\n",
    "1 - to add elements into temp - (d)\n",
    "2 - to pop elements from arr - (d)\n",
    "3 - to add arr and temp - (1)\n",
    "\n",
    "Total steps = 2*d + 1\n",
    "\n",
    "Additional space required = (d)\n",
    "\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 4, 5, 1, 2]\n"
     ]
    }
   ],
   "source": [
    "def arr_rot_2(arr, d):\n",
    "    for i in range(d):\n",
    "        x = arr[0]\n",
    "        arr.append(x)\n",
    "        arr.pop(0)\n",
    "    print(arr)\n",
    "    \n",
    "arr_rot_2([1,2,3,4,5], 2)  \n",
    "\n",
    "'''\n",
    "In the above logic, total number of steps are \n",
    "\n",
    "1 - to store an element into a variable - (d)\n",
    "2 - to append elements to array - (d)\n",
    "3 - to pop elements - (d)\n",
    "\n",
    "Total steps = 3*d\n",
    "\n",
    "Additional space required = (1)\n",
    "\n",
    "'''"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
