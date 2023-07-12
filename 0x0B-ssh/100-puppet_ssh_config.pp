# configure the server

file { '/etc/ssh/ssh_config':
  ensure => 'file',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0644',
  content => "PasswordAuthentication no\n",
}
