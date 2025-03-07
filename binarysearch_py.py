
        "def binary_search(arr, low, high, x):\n",
        "\n",
        "\n",
        "    if high >= low:\n",
        "\n",
        "        mid = (high + low) // 2\n",
        "        if arr[mid] == x:\n",
        "            return mid\n",
        "\n",
        "        elif arr[mid] > x:\n",
        "            return binary_search(arr, low, mid - 1, x)\n",
        "\n",
        "\n",
        "        else:\n",
        "            return binary_search(arr, mid + 1, high, x)\n",
        "\n",
        "    else:\n",
        "\n",
        "        return -1\n",
        "\n",
        "arr = [ 2, 3, 4, 10, 40 ]\n",
        "x = 10\n",
        "\n",
        "result = binary_search(arr, 0, len(arr)-1, x)\n",
        "\n",
        "if result != -1:\n",
        "    print(\"Element is present at index\", str(result))\n",
        "else:\n",
        "    print(\"Element is not present in array\")\n"
