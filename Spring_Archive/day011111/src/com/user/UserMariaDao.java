package com.user;

import java.util.ArrayList;

import com.frame.Dao;

public class UserMariaDao implements Dao<String, User> {

	@Override
	public void insert(User v) throws Exception {
		System.out.println(v + "UserMariaDao Inserted...");
	}

	@Override
	public void update(User v) throws Exception {
		System.out.println(v + "UserMariaDao Updated...");
	}

	@Override
	public void delete(User v) throws Exception {
		System.out.println(v + "UserMariaDao Deleted...");
	}

	@Override
	public User select(String k) throws Exception {
		return new User("����","¯¯","123123");
	}

	@Override
	public ArrayList<User> selectAll() throws Exception {
		ArrayList<User> list = new ArrayList<User>();
		
		list.add(new User("����","¯¯","1231234"));
		list.add(new User("����","¯¯","12312345"));
		list.add(new User("����","¯¯","123123456"));
		list.add(new User("����","¯¯","1231234567"));
		
		return list;
	}

}
