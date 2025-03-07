{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyORBJBGCTHS3CKiBlZCeDVH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aravindhan222/algorithm_lab/blob/main/binarysearch_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zTEAVtv2Bcqx",
        "outputId": "53b6f547-18f5-4611-fdac-af8359a0c537"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Element is present at index 3\n"
          ]
        }
      ],
      "source": [
        "\n",
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
      ]
    }
  ]
}