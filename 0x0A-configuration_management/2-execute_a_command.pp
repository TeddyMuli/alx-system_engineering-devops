#kills a process

exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
