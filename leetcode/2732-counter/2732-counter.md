<h1>2732 - Counter</h1><h2>Difficulty: Easy - <a href="https://leetcode.com/problems/counter/">counter</a></h2><p>Given an integer&nbsp;<code>n</code>,&nbsp;return a <code>counter</code> function. This <code>counter</code> function initially returns&nbsp;<code>n</code>&nbsp;and then returns 1 more than the previous value every subsequent time it is called (<code>n</code>, <code>n + 1</code>, <code>n + 2</code>, etc).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
n = 10 
[&quot;call&quot;,&quot;call&quot;,&quot;call&quot;]
<strong>Output:</strong> [10,11,12]
<strong>Explanation: 
</strong>counter() = 10 // The first time counter() is called, it returns n.
counter() = 11 // Returns 1 more than the previous time.
counter() = 12 // Returns 1 more than the previous time.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
n = -2
[&quot;call&quot;,&quot;call&quot;,&quot;call&quot;,&quot;call&quot;,&quot;call&quot;]
<strong>Output:</strong> [-2,-1,0,1,2]
<strong>Explanation:</strong> counter() initially returns -2. Then increases after each sebsequent call.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-1000<sup>&nbsp;</sup>&lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= calls.length &lt;= 1000</code></li>
	<li><code>calls[i] === &quot;call&quot;</code></li>
</ul>
