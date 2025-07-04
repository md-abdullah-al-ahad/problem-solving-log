<h1>1524 - String Matching in an Array</h1><h2>Difficulty: Easy - <a href="https://leetcode.com/problems/string-matching-in-an-array/">string-matching-in-an-array</a></h2><p>Given an array of string <code>words</code>, return all strings in<em> </em><code>words</code><em> </em>that are a <span data-keyword="substring-nonempty">substring</span> of another word. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;mass&quot;,&quot;as&quot;,&quot;hero&quot;,&quot;superhero&quot;]
<strong>Output:</strong> [&quot;as&quot;,&quot;hero&quot;]
<strong>Explanation:</strong> &quot;as&quot; is substring of &quot;mass&quot; and &quot;hero&quot; is substring of &quot;superhero&quot;.
[&quot;hero&quot;,&quot;as&quot;] is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;leetcode&quot;,&quot;et&quot;,&quot;code&quot;]
<strong>Output:</strong> [&quot;et&quot;,&quot;code&quot;]
<strong>Explanation:</strong> &quot;et&quot;, &quot;code&quot; are substring of &quot;leetcode&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;blue&quot;,&quot;green&quot;,&quot;bu&quot;]
<strong>Output:</strong> []
<strong>Explanation:</strong> No string of words is substring of another string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code> contains only lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
</ul>
