# configure the server

file { '/home/ubuntu/.ssh/config':
  ensure => 'file',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  content => "Host ubuntu\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n",
}
