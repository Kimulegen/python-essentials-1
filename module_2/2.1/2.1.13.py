# normal
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# 1. minimize the number of `print()` function invocations by inserting the `\n` sequence into the strings
print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****", sep="\n")

# 2. make the arrow twice as large (but keep the proportions)
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("*****       *****")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *********")

# 3. duplicate the arrow, placing both arrows side by side
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)

# 4. remove any of the quotes, and look carefully at Python's response.
print("    *")
print("   * *"
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
# SyntaxError: '(' was never closed

# 5. change any of the `print` words into something else, differing only in case - what happens now?
Print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
# NameError: name 'Print' is not defined

# 6. replace some of the quotes with apostrophes; watch what happens carefully
print("    *")
print("   * *")
print("  *   *")
print(' *     *')
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")